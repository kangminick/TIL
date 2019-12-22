# 1. Telegram Chatbot

- ### `app.py` : Telegram 챗봇 예제 `python file`

  ```python
  from flask import Flask, render_template, request
  # flask 와 관련된 모듈을 import
  from decouple import config
  # decouple모듈을 사용한 이유
  # .env파일에 저장되어 있는 것들: API Token값, CHAT_ID와 같은 값들은 모두 숨겨야하는 중요한 정보다.
  # 그래서, 중요한 정보를 .env파일에 숨겨두고, decouple의 config모듈을 이용하여 로컬에서는 자신의 API Key값과 CHAT_ID값을 이용하여 매핑된다.
  # 그리고, .env파일은 .gitigonre 파일을 통해서 git에 push하지 않을 것이다.
  
  import requests
  # requests는 현재 나의 python함수에서 웹 페이지로 요청을 보내게 해주는 모듈
  # flask 모듈이 제공하는 request는 해당 URL로 들어오는 요청에 대해서 처리하는 모듈
  
  app = Flask(__name__)
  
  url = "https://api.telegram.org/bot"
  token = config('TELEGRAM_BOT_TOKEN')
  # 같은 경로의 .env 파일에 저장된 TELEGRAM_BOT_TOKEN에 저장된 값을 token에 저장한다.
  chat_id = config('CHAT_ID')
  # 같은 경로의 .env 파일에 저장된 CHAT_ID에 저장된 값을 chat_id에 저장한다.
  
  @app.route('/')
  def hello():
      return 'Hello World'
  	# 맨 처음 화면
  
  @app.route('/send')
  def send():
      text = request.args.get('text')
      # send URL에 요청과 함께 들어온 text라는 인자를 python text변수에 저장한다.
      
      requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')
      # fstring으로 정보를 요청할 URL을 가공한다.
      
      return render_template('send.html', text=text)
  	# send.html을 만들어서 보여주라는 명령어지만, 실제로는 send.html파일이 없다.
      # 사실, send함수의 목적은 chat_id로 text라는 메세지를 보내는데에 목적이 있기 때문에 이렇게 코드를 짰다.
  
  @app.route('/write')
  def write():
      return render_template('write.html')
  	# write.html을 불러온다.
      # write.html은 /send?text=[text폼에 입력한 메세지]를 호출한다
  
  @app.route(f'/{token}', methods=["POST"])
  # [기본 URL]/[bot의 token값] 으로 들어오는 모든 정보들은 bot에게 들어오는 요청의 정보와 같다.
  # 이 정보들은 telegram api docs에 따르면, JSON형태로 들어온다고 명시되어 있다.
  
  def telegram():
      data = request.get_json()
      # 요청으로 들어오는 JSON형태의 정보들을 data에 저장한다.
      
      text = data['message']['text']
      chatID = data['message']['chat']['id']
      # request message의 JSON형태를 분석하여
      # 내가 원하는 data인 message의 text와
      # message를 보낸 user_id를 추출한다.
      
      if(text == "안녕"):
          return_text = "안녕하세요."
      elif text=="로또":
          numbers = range(1, 46)
          number = random.sample(numbers, 6)
          return_text = sorted(number)
      else:
          return_text = text
      # 어떤 text가 들어오느냐에 따라서 return_text를 달리해준다.
      
      requests.get(f'{url}{token}/sendMessage?chat_id={chatID}&text={return_text}')
      return "ok", 200
  
  if __name__==('__main__'):
      app.run(debug=True)
  ```

# 2. `ngrok`을 이용한 `Python Webserver` 배포

1. `webhook` : [목적Server]와 갈고리로 [나의 Server]를 연결하여 [목적Server]에 요청이 들어오는 등 변화가 있다면, 그러한 변화를 [나의 Server]에도 알려주도록 하는 기능을 `webhook`이라고 한다.
2. `Telegram`은 [Telegram Server]의 변화를 [나의 Server]에 알려주는 API도 제공하고 있다. (`setWebhook`)
3. 이를 이용하여 [나의 Server]를 임시로 구동하기 위해 8시간 동안 구동이 되는 Server인 `ngrok`을 다운로드 받고, 사용하였다.
4. `ngrok` 구동 방법: `cmd` 창에서 `ngrok` 이 저장된 경로로 이동 후,`ngrok.exe http 5000`명령으로 5000포트로 임시 [나의 Server]를 구동하였다.
5. `local`환경에서 `webhook.py`를 실행하여 [Telegram Server]와 [나의 Server]간 연결관계를 형성한다.

# 3. `pythonanywhere.com` 을 이용한 `Python Webserver` 배포

1. `Files`메뉴 - `mysite` 디렉토리에 `flask_app.py`에 내가 서버로 사용할 코드를 작성하고, 저장
2. `Consoles`메뉴 - `Bash`선택 - `pip3 install python-decouple --user`
3. `Files` 메뉴 - `mysite` 디렉토리에 `.env` 파일 생성 및 토큰 값 저장
4. `Files` 메뉴 - `mysite` 하위의 `templates` 디렉토리를 생성하고, `templates` 디렉토리에 필요한 `.html` 파일들을 저장한다.
5. `local`환경에서 `webhook.py`를 실행하여 [Telegram Server]와 [나의 Server]간 연결관계를 형성한다.
6. `Web` 메뉴 - `Reload [나의 Server주소]`를 클릭하여 현재까지 저장된 정보를 모두 update해준다.

- ### `webhook.py` : [Telegram Server]와 [나의 Server] 간의 연결관계를 형성하는 `python file`

  ```python
  from decouple import config
  import requests
  
  token = config('TELEGRAM_BOT_TOKEN')
  # 나의 key값을 config함수를 통해 .env파일의 'TELEGRAM_BOT_TOKEN'를 가져와서 token에 저장한다.
  
  url = "https://api.telegram.org/bot"
  
  # ngrok_url = "https://cca4ba97.ngrok.io"
  # ngrok을 이용할 때 사용하는 코드, ngrok_url = [ngrok에서 생성한 https 주소]
  
  paw_url = "https://milanoderby.pythonanywhere.com"
  # pythonanywhere을 이용할 때 사용하는 코드, 반드시, [https]로 주소를 넣어줄 것!
  
  # data = requests.get(f'{url}{token}/setWebhook?url={ngrok_url}/{token}')
  # ngrok을 이용할 때 사용하는 코드
  
  data = requests.get(f'{url}{token}/setWebhook?url={paw_url}/{token}')
  # pythonanywhere를 이용할 때 사용하는 코드
  # requests 모듈과 Telegram API의 setWebhook를 이용하여 우리의 원래 URL을 NGROK URL과 연결한다.
  
  print(data.text)
  # 성공적으로 연결관계를 형성했는지 출력한다.
  ```

- ### `.env` : `API key` 값이나 `사용자의 CHAT_ID`와 같은 중요 정보를 저장하는 파일

  ```python
  ex)
  CHAT_ID = "1283912830"
  TELEGRAM_BOT_TOKEN = "127389:ASDFASDKLFASFJSDFKAJSDF"
  ```
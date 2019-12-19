# Python Flask

- Flask web server 구축 코드

```shell
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/') # root로 요청을 보냄
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
```

- Git에서 서버 구동 명령어

```shell
$ env FLASK_APP=hello.py flask run
```

- 단순 py파일 실행으로 서버 구동 하기 위해 추가해야할 명령어

```shell
if __name__ == "__main__": #__name__은 flask 생성시 선정한 이름
    app.run(debug=True)
```

! + tab 쓰면 html 기본 형식 써짐
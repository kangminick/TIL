# Python Flask

### 1. flask 설치하기

```
 $ pip install flask==1.0.0 
```

'Flask | The Pallets Projects' 페이지에서 소스코드를 가져옴

(참고: https://www.palletsprojects.com/p/flask/)

- Flask web server 구축 코드

```python
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

### 2. HTML로 출력하기

`render_template('hi.html')`: html파일을 불러옴

[예제1] 변수를 받아서 HTML로 출력

```python
# hello.py 파일
from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/hi')
def hi():
    name = "김강민"
    return render_template('hi.html', html_name = name)

if __name__=="__main__":
    app.run(debug=True)
<!-- hi.html 파일 -->
<body>
    <h1>{{html_name}}</h1>
</body>
```

[예제2] 주소창으로 String변수를 받음

http://127.0.0.1:5000/greeting.html

```python
# hello.py 파일
@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name=name
    return render_template('greeting.html',html_name=def_name)
<!-- hi.html 파일 -->
<body>
    <h1>만나서 반갑습니다. {{html_name}}님</h1>
</body>
```

[예제3] 주소창으로 Int변수를 받음

```python
# hello.py 파일
@app.route('/cube/<int:num>')
def cube(num):
    def_num = num
    def_cube = num**3
    return render_template('cube.html',html_num=def_num,html_cube=def_cube)
<!-- hi.html 파일 -->
<body>
    <h2>{{html_num}}의 3제곱은</h2>
    <h2>{{html_cube}} 입니다.</h2>
</body>
```

### 3. 반복문/조건문 사용하기

> **html**파일에서 **python**문법 사용하기

- {% %}으로 감싸줘야함

- 반복문, 조건문의 끝을 말해줘야함

  `{% endfor %}` `{% endif %}`

```python
@app.route('/movies')
def movies():
    movies= ['조커','겨울왕국2','터미네이터','어벤져스']
    return render_template('movie.html', movies=movies)
<body>
    {% for movie in movies %}
        <li>{{ movie }}</li>
    {% endfor %}
</body>
```

[예제] `.py`에서 `.html`로 리스트를 받아서 if문과 for문 사용하기

```python
@app.route('/movies')
def movies():
    movies= ['조커','겨울왕국2','터미네이터','어벤져스']
    return render_template('movie.html', movies=movies)
<body>
    {% for movie in movies %}
        {% if movie =='조커' %}
            <li>{{movie}} (이 영화 진짜 재밌어!)</li>
        {% elif movie == '겨울왕국2' %}
            <li>{{movie}} (역시 겨울왕국!)</li>
        {% else %}
            <li>{{movie}}</li>
        {% endif %}
    {% endfor %}
</body>
```

### 4. form태그로 값 보내기

[예제] */ping* 에서 */pong*으로 값 보내기

1. */ping* 에서 keyword 값을 받아 */pong* 으로 보냄
2. .py

```python
#ping_pong.py 파일

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    data=request.args.get("keyword")
    return render_template('pong.html', data = data)
<!-- ping.html 파일 -->

<body>
    <h1>Here is Ping!!</h1>
    <form action="/pong">
        <input type="text" name="keyword">
        <input type="submit">
    </form>
</body>
<!-- pong.html 파일 -->

<body>
    <h1>여기는 Pong 입니다!</h1>
    {{data}}
</body>
```
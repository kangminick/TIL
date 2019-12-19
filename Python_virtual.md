# Python 가상환경

- 가상환경 셋팅

```
$ python -m venv [지정이름]
```

- 가상환경 활성화/Mac의 경우 Scripts 대신 bin 사용

```powershell
$ source [지정이름]/Scripts/activate
```

- 가상환경 비활성화

```shell
$ deactivate
```

- 가상환경을 삭제하고 싶을 경우
  - 폴더 삭제! rm rf - 폴더명
- 모듈 버젼명까지 확인하고 관리하는 법

```shell
#pip list
$ pip freeze
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```

- Flask 구버젼 까는 법

```shell
$ pip install flask==1.0.0
```
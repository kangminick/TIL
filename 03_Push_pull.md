# Git Test

- b.txt 파일 만들기

```shell
$ touch b.txt
```

- git 상태확인 메세지

```shell
$ git status
```

- git log 확인하기

```shell
$ git log
$ git log --oneline // 한줄 출력
```

---

- git 원격저장소 주소 지정하기

```shell
$ git remote add origin 주소
```

- git 원격저장소 주소 확인하기

```shell
 $ git remote
 $ git remote -v // 자세한 내용 출력 옵션
```

---

- github에 올리는 명령어

```shell
$ git push origin master
```

- github에 올린 코드 가져오는 명령어(최초 연결시)

```shell
$ git clone 주소 (github에서 복사)
```

- github에 올린 코드중 수정된 부분만 가져오기

```shell
$ git pull origin master
```

---

- git repository 바꾸는 명령어

```shell
$ git remote rename 현재이름 바꿀이름
```


## 1. Git Branch

- 다른 가상공간 생성(master 외에)

```shell
$ git branch [이름]
```

- 다른 branch 공간 이동

```shell
$ git switch [이름]
$ git checkout [이름]
```

- 현재 속한 branch 공간 확인방법

  - prompt (맨 끝)

  - ```shell
    $ git log --oneline
    ```

  - ```shell
    $ git branch
    ```

- Branch 생성 및 바로 이동 명령어

  ```shell
  $ git switch -c (이름)
  ```

  

### 추가 학습 사항

- commit 기준
  - 전 :  어떤 branch에서도 파일은 보임
  - 후 :  commit을 실행한 branch 세계에서만 확인 가능

## 2. Git Merge

- Git branch 병합 명령어

```shell
$ git merge (병합할 branch)
```

**주의사항** : 항상 상위 세계 branch에서 합쳐야함 ex) master에서 new를 합침

- **Fast-forward : master가 브랜치의 파일을 commit을 안한상태에서 merge**

  - 이 방법 사용하지 않겠다는 명령어

    - ```shell
      $ git merge (이름) --no--ff
      ```

- **Auto merge**

  Merge 시점에 양쪽 브랜치에 commit이 있지만 자연스럽게 master 브랜치로 merge 될때

- **Merge Conflict 발생**

  Merge 시점에 양쪽 브랜치에 commit이 있고, 동일한 파일 내에 상충하는 내용이 있을 경우

- **GitHub에서 Merge 할 수 있음 !**



## 3. Git branch 삭제

- Git branch 삭제 명령어

```shell
$ git branch -d (삭제할 branch 이름)
```

#### Merge Confilct

---

merge시 갈등이 생기는 경우

#### Conflict 발생

---

같은 파일에서 다른 내용이 있을 경우

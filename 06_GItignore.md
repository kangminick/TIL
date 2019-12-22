

## Gitignore

- `Git push` 할 때, 불필요한 파일은 `push` 안하게 하는 방법
- `http://gitignore.io/` 에 들어가서 내가 사용하는 환경에 관련된 기본 설정파일들에 대해 명시를 해주고, 생성버튼을 누른다.
- 불필요한 파일의 종류
  1. vscode가 만들어내는 `.vscode`
  2. eclipse가 만들어내는`.metadata`
  3. 등 git에 올리지 않아도 되는 설정파일
- `requirements.txt` 같은 파일은 `python` 에서 어떤 개발모듈들을 사용했는지를 알려주어야 하므로 `push`해줘야하는 파일이다. 배포환경에 대한 정보를 알려주는 정보이기 때문이다.


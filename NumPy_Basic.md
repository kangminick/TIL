# NumPy_Basic

```python
data = randn(2,3) #랜덤 numpy 2 x 3 행렬 생성

data[0][1] #1행 2열의 값을 출력, pointing 차원축소가 됨, 값만을 출력한다고 생각하면됨
data[0,1] #위와 같음
#출력값을 통해 위아래 차이를 확인
data[:1,1:2] #slice한 것, 차원이 유지됨 (연속색인?) 

data.shpae #(2,3)행렬인 것을 확인가능
data.ndim #차원 확인가능 dimension
data[:, :-1] #1,2 행 출력
data[:1, :-1] #(1,1) (1,2)출력
data.reshape(3,2) # 3x2행렬로 변환
data.T # 행렬에 Trans 취한것 data^T
randn(2,3,2) #3차원 행렬 2x3x2 앞방향 혹은 뒷방향 선택해서 이해하도록. 뒤부터 열 행 Z
arr2.reshape(3,4) #위에서부터 4개 3줄로 변환 즉, 3행 4열로 가로로 순서대로 값 들어감
data + [[1,2,3]] #각 열 마다 1, 2, 3이 더해짐
data + [2] #모든 자리에 2를 더함
#뒷자리 숫자가 일치해야 error 발생 안함. 또는 한자리가 서로 1이어야 가능
data + [[2], [3]]

print(data.shape, data.size)
data.dtype
len(data) == data.shape[0]#data의 첫 요소(행) [1,2,3]이면 1이 len(data)의 값과 같음

arr = np.array([
    [1,2,3],
    [4,5,6]
])
arr
arr[1,:2] #arr의 2행의 두번째 열까지 출력 [4 ,5] arr[1][:2]는 사용하지 말 것

arr[1,:2] = 0
arr #arr의 2행의 두번째 열까지가 0으로 됨, 값 대입인듯

v1 = arr[1,:2]
v1[:] = 0
arr #위와 같음 신기.

v2 = arr[1,:2].copy()
v2[:] = 1
arr #copy를 쓰면 안됨.

arr[0,[0,1]] #1행의 1,2열

v3 = arr[0,[0,1]]
v3[:] = 0
arr #arr변하지 않음, 불연속 색인은 안됨, 불연속 색인은 copy()처럼 동작

v4 = arr[0, :2]
v4[:] = 0
arr #arr의 1행 1,2열이 0으로 됨, 즉 연속색인은 됨, 원래 값이 변경됨




```

### ndarray를 생성하는 numpy 함수들

---

사용할 때는 np.함수명으로 사용한다.

- array	: 입력 데이터를 ndarray로 변환. dtype 미 지정시, 자료형에서 추론
  asarray	: 입력 데이터를 ndarray로 변환. 입력 데이터가 ndarray일 경우 그대로 표시
  arange	: 내장range 함수와 유사하지만 리스트 대신 ndarray를 반환
  ones	: 주어진 dtype과 shape을 가지는 배열 생성. 성분을 모두 1로 초기화
  ones_like	: 주어진 배열과 동일한 shape과 dtype을 갖는 배열을 생성. 1로 초기화
  zero	 : ones와 같지만 0으로 채운다
  zeros_like	: ones_like와 같지만 0dmfh codnsek
  empty	: 메모리를 할당하지만 초기화가 없음
  empty_like	: 메모리를 할당하지만 초기화가 없음
  eye(N,M,k=0)	: 1, 0의 값을 갖는 대각 NxM 대각 행렬 생성. k에 따라 대각이 이동
  identity	: n x n 단위행렬 생성
  linspace	: start, stop, size를 설정하면 ndarray로 생성
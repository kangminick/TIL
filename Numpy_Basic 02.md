# Numpy_Basic 02

```python
arr.sort() #(l,m,n)일때, n을 기준으로 오름차순
arr.sort(1) #위와 같음
arr.sort(0) #m을 기준으로 오름차순
arr.sort(-1) #m을 기준으로 내림차순

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names) #중복제거되어 나옴
#출력 array(['Bob', 'Joe', 'Will'], dtype='|S4')
sorted(set(names)) #위와 같지만 list로 나옴

values = np.array([6, 0, 0, 3, 2, 5, 6])
np.in1d(values, [2, 3, 6]) #포함된거 찾아줌
#array([ True, False, False,  True,  True, False,  True], dtype=bool)
```

# Pandas

```python
df.colums #열제목
df.index #행제목
df.series #내용물 colums의 영향을 받는다. ex) colums 6이면 6series(index가 같은)라고 한다.
#1d array(dtype) + schema(index, label, name)로 구성되어 있다.

df.head().T #Transpose




```


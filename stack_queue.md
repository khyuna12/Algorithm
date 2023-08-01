## 가장 기본이 되는 자료구조: 스택과 큐

### 스택 자료구조
- 먼저 들어온 데이터가 나중에 나가는 선입후출 자료구조

- 입구와 출구가 동일

- 스택 구현 예제(python)
```python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력
```

- 실행 결과
```
deque([1, 3, 2, 5])
deque([5, 2, 3, 1])
```

<br>

### 큐 자료구조
- 먼저 들어온 데이터가 먼저 나가는 선입 선출 형식의 자료 구조

- 입구와 출구가 모두 뚫려있는 터널같은 형

- 큐 구현 예제(python)
```python
from collections import deque

# Queue 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```

- 실행 결과
```
deque([3, 7, 1, 4])
deque([4, 1, 7, 3])
```


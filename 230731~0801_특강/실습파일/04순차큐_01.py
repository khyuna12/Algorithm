## 함수


## 변수
# stack과 거의 비슷
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
# enQueue()
rear += 1
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
rear += 1
queue[rear] = '문별'
print('출구 <--', queue, '<-- 입구')

#deQueue()
front += 1
data = queue[front]  # 저장? 해야함 (손님나가고 닦아준다)
queue[front] = None
print('손님 이리로: ', data)
front += 1
data = queue[front]
queue[front] = None
print('손님 이리로: ', data)
front += 1
data = queue[front]
queue[front] = None
print('손님 이리로: ', data)
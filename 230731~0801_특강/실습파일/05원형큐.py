## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear+1) % SIZE == front):
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐 꽉!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def isQueueEmpty(): # 순차 큐와 동일
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 텅~')
        return
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peak():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 텅~')
        return
    return queue[(front + 1) % SIZE]  # 맨 앞줄에 있는(가장 먼저 나올) 사람 보기


## 변수
# stack과 거의 비슷
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0  # 차이점

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
# enQueue('선미')
print('출구 <--', queue, '<-- 입구')

retData = deQueue()
print('식사 손님: ', retData)
retData = deQueue()
print('식사 손님: ', retData)
print('출구 <--', queue, '<-- 입구')

enQueue('재남')
enQueue('정국')
print('출구 <--', queue, '<-- 입구')  # 한 칸 None인 상태 => 꽉 찬 상태
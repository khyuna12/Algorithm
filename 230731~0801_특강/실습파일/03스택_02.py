## 함수
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE - 1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull() == True):
        print('스택 꽉 참')
        return
    top += 1
    stack[top] = data
    return

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty() == True):
        print('스택 텅 빔')
        return None
    data = stack[top]
    stack[top] = None  # del(stack[top]) 하면 스택 사이즈 달라짐
    top -= 1
    return data

def peak():
    global SIZE, stack, top
    if (isStackEmpty() == True):
        print('스택 텅 빔')
        return None
    return stack[top]

## 변수
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

## 메인
push('커피')
push('녹차')
# push('꿀물')
# push('콜라')
# push('환타')
# print('바닥: ', stack)
#
# push('개토레이')
print('바닥: ', stack)

retData = pop()
print('팝--> ',retData)

print('다음 예정: ', peak())

retData = pop()
print('팝--> ',retData)
retData = pop()
print('팝--> ',retData)
print('바닥: ', stack)
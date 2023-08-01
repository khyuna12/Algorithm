## 함수
import random
def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary) - 1
    while(start <= end):
        mid = (start + end) // 2
        if (fData == ary[mid]):
            return mid
            break
        elif (fData > ary[mid]):
            start = mid + 1
        else:
            end = mid - 1
    return pos

## 변수
dataAry = [random.randint(30, 190) for _ in range(8)]
findData = random.choice(dataAry)
dataAry.sort()

## 메인
print('배열 --> ', dataAry)
position = binSearch(dataAry, findData)
if (position == -1):
    print(findData, '없음')
else:
    print(findData, '는', position, '위치에 있어요')
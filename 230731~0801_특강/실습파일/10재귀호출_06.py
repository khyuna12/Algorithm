## 함수
# 별 모양 출력하기
def printStar(n):
    if n > 0:
        printStar(n-1)
        print('★' * n)

## 변수

## 메인
printStar(5)

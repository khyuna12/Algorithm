## 함수
# 팩토리얼 구하기
def factorial(num):
    if (num <= 1):
        return 1
    return num * factorial(num - 1)

## 변수

## 메인
print(factorial(10))
print(factorial(5))

## 함수
# 우주선 발사 카운트다운
def countdown(n):
    if n == 0:
        print('발사!')
    else:
        print(n)
        countdown(n - 1)

## 변수

## 메인
countdown(5)

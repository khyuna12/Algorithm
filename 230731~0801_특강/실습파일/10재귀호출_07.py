## 함수
# 구구단 출력하기
def gugu(dan, num):
    print('%d x %d = %d' % (dan, num, dan*num))
    if num < 9:
        gugu(dan, num + 1)

## 변수

## 메인
for dan in range(2, 10):
    print('## %d단 ##' % dan)
    gugu(dan, 1)

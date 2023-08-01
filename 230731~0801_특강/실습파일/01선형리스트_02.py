## 함수 선언부
def add_data(friend):
    katok.append(None)  # 1단계: 빈칸 추가
    klen = len(katok)
    katok[klen - 1] = friend # 2단계: 데이터 입력

def inset_data(position, friend):
    # 1단계: 빈칸 추가
    katok.append(None)
    klen = len(katok)
    # 2단계: 마지막 칸부터 삽입할 칸까지 한칸씩 뒤로 이동
    '''
    katok[6] = katok[5] # 모모
    katok[5] = None
    katok[5] = katok[4] # 지효
    katok[4] = None
    katok[4] = katok[3] # 사나
    katok[3] = None
    '''
    for i in range(klen - 1, position, -1):  # 어려움
        katok[i] = katok[i - 1]
        katok[i - 1] = None
    # 3단계: 위치에 친구 입력
    katok[position] = friend

def delete_data(position):
    # 1단계: 데이터 지우기
    katok[position] = None
    klen = len(katok)
    # 2단계: 한칸씩 앞으로 당기기
    '''
    katok[4] = katok[5] # 지효
    katok[5] = None
    katok[5] = katok[6] # 모모
    katok[6] = None    
    '''
    for i in range(position + 1, klen, 1):
        katok[i - 1] = katok[i]
        katok[i] = None
    # 3단계: 마지막 칸 제거
    del(katok[klen - 1])

## 전역 변수부
katok = []

## 메인 코드부
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)

add_data('모모')
print(katok)

inset_data(3, '미나')
print(katok)
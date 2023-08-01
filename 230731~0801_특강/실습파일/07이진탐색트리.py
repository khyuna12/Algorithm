## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)  # 파이썬에서는 안 중요!

for name in nameAry[1:]: # ['레드벨벳', '마마무',...
    node = TreeNode()
    node.data = name

    current = root
    while True:  # 몇 번 반복하는지 모름
        if (name < current.data):
            if (current.left == None):
                current.left = node
                break
            else:
                current = current.left
        else:
            if (current.right == None):
                current.right = node
                break
            else:
                current = current.right

    memory.append(node)

print('이진 탐색 트리 완료!')

findName = '마마무'
current = root
while True:
    if (findName == current.data):
        print(findName, '찾음')
        break
    elif (findName < current.data):
        if (current.left == None):
            print(findName, '없음')
            break
        current = current.left
    else:
        if(current.right == None):
            print(findName, '없음')
            break
        current = current.right
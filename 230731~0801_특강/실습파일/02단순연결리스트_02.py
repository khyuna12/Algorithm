## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre
    # Case1 : head 앞에 삽입하는 경우 (다현, 화사)
    if (head.data == findData):
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node) # 안 중요
        return
    # Case2: 중간 노드 앞에 삽입 (사나, 솔라)
    current = head
    while(current.link != None):
        pre = current
        current = current.link
        if (current.data == findData):
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)  # 안 중요
            return
    # Case3: 없는 노드 앞에 삽입(= 추가) (재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)  # 안 중요
    return

def deleteNode(deleteData):
    global memory, head, current, pre
    # Case1: 머리 삭제 (다현)
    if (head.data == deleteData):
        current = head
        head = head.link
        del(current)
        return
    # Case2: 중간 노드 삭제 (쯔위)
    current = head
    while(current.link != None):
        pre = current
        current = current.link
        if (current.data == deleteData):
            pre.link = current.link
            del(current)
            return
    # Case3: 없는 노드 삭제(=그대로)
    return  # 안 써도 됨

def findNode(findData):
    global memory, head, current, pre
    current = head
    if (current.data == findData):
        return current
    while (current.link != None):
        current = current.link
        if (current.data == findData):
            return current
    return Node()

## 전역 변수
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']  # 실제 사용 데이터 모음

## 메인
# 첫 번째 데이터 입력
node = Node()  # 1. 빈 노드 생성
node.data = dataArray[0]  # 2. 데이터 입력
head = node  # 3. 첫번째 노드를 헤드로 지정
memory.append(node)  # 안 중요!(노드를 메모리에 넣음)

# 두 번째 이후 데이터 입력
for data in dataArray[1:]:  # ['정연', '쯔위', ... ]
    pre = node  # 0. 기존 노드를 임시 저장
    node = Node()  # 1. 빈 노드 생성
    node.data = data  # 2. 데이터 입력
    pre.link = node  # 3. 이전의 링크를 새 노드에 대입
    memory.append(node)

printNodes(head)

# insertNode('다현', '화사')  # '다현'을 찾아서 그 앞에 '화사'를 넣는 방식
# printNodes(head)
#
# insertNode('사나', '솔라')
# printNodes(head)
#
# insertNode('재남', '문별')
# printNodes(head)

# deleteNode('다현')
# printNodes(head)

# deleteNode('쯔위')
# printNodes(head)

# deleteNode('재남')
# printNodes(head)

fNode = findNode('사나')
print(fNode.data, '뮤비가 나옵니다')
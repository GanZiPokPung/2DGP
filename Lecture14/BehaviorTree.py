
level = 0
def indent():
    global level
    level += 1

def unindent():
    global level
    level -= 1

def print_indent():
    for i in range(level):
        print("    ", end='')


class BehaviorTree:
    FAIL, RUNNING, SUCCESS = -1, 0, 1

    def __init__(self, root_node):
        self.root = root_node

    def run(self):
        self.root.run()

    def print(self):
        self.root.print()


class Node:
    def add_child(self, child):
        self.children.append(child)
    def add_children(self, *children):
        for child in children:
            self.children.append(child)

# 여러 상황, 행동중에 하나만 해야할때 자주 쓰인다.
class SelectorNode(Node):
    def __init__(self, name):
        self.children = []
        self.name = name
        self.prev_running_pos = 0

    def run(self):

        # 노드의 child들을 순차적으로 돌며
        for pos in range(self.prev_running_pos, len(self.children)):
            # run 하고 run의 반환값을 result에 받는다.
            result = self.children[pos].run()
            # 만약 RUNNING 상태라면 현재 노드 위치를 저장하고 RUNNING을 반환
            if BehaviorTree.RUNNING == result:
                print('RUNNING')
                self.prev_running_pos = pos
                return BehaviorTree.RUNNING
            # SUCCESS 상태라면 노드 위치를 0으로 하고 SUCCESS를 반환
            elif BehaviorTree.SUCCESS == result:
                print('SUCCESS')
                self.prev_running_pos = 0
                return BehaviorTree.SUCCESS
        # 만약 어디에도 속하지 않는다면 FAIL 끝남
        # 모든 자식 노드가 FAIL이면 이 노드도 FAIL
        print('FAIL')
        self.prev_running_pos = 0
        return BehaviorTree.FAIL

    def print(self):
        print_indent()
        print("SELECTOR NODE: " + self.name)
        indent()
        for child in self.children:
            child.print()
        unindent()

# 어떠한 상황,행동 등을 순차적으로 처리해야 할때 자주 쓰인다.
class SequenceNode(Node):
    def __init__(self, name):
        self.children = []
        self.name = name
        self.prev_running_pos = 0

    def run(self):
        for pos in range(self.prev_running_pos, len(self.children)):
            result = self.children[pos].run()
            if BehaviorTree.RUNNING == result:
                print('RUNNING')
                self.prev_running_pos = pos
                return BehaviorTree.RUNNING
            elif BehaviorTree.FAIL == result:
                print('FAIL')
                self.prev_running_pos = 0
                return BehaviorTree.FAIL

        print('SUCCESS')
        # 모든 자식 노드가 SUCCESS이면 이 노드도 SUCCESS
        self.prev_running_pos = 0
        return BehaviorTree.SUCCESS

    def print(self):
        print_indent()
        print("SEQUENCE NODE: " + self.name)
        indent()
        for child in self.children:
            child.print()
        unindent()


class LeafNode(Node):
    def __init__(self, name, func):
        self.name = name
        self.func = func

    # Leaf Node는 child 노드들이므로 자식 노드를 추가할 수 없다.
    def add_child(self, child):
        print("ERROR: you cannot add child node to leaf node")

    def add_children(self, *children):
        print("ERROR: you cannot add children node to leaf node")

    def run(self):
        return self.func()

    def print(self):
        print_indent()
        print("LEAF NODE: " + self.name)




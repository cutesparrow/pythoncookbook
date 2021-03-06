#你想构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法。
class Node:
    def __init__(self,value):
        self.value = value
        self.children = []
    def __iter__(self):
        return iter(self.children)
    def deepFirst(self):
        yield self
        for i in self:
            yield from i.deepFirst()
    def addChild(self,node):
        self.children.append(node)
    def __repr__(self):
        return 'Node({})'.format(self.value)

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.addChild(child1)
    root.addChild(child2)
    child1.addChild(Node(3))
    child1.addChild(Node(4))
    child2.addChild(Node(5))

    for ch in root.deepFirst():
        print(ch)

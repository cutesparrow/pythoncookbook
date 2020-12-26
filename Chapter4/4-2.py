class Node():
    def __init__(self,value):
        self.value = value
        self.children = []
    def __iter__(self):
        return iter(self.children)
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
    for i in root:
        print(i)

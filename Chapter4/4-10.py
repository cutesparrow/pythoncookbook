my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print('index = {},value = {}'.format(index, value))
data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
for index,(i,j) in enumerate(data):
    print('{}:{},{}'.format(index,i,j))

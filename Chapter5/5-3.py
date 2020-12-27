#你想使用 print() 函数输出数据，但是想改变默认的分隔符或者行尾符。
print(3,3,2,'something',sep=':',end='.')
row = [1,2,3,4,5]
print(row,sep=':')
print(*row,sep=':')

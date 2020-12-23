#怎样从一个集合中获得最大或者最小的 N 个元素列表？
import heapq
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheaper = heapq.nsmallest(3,portfolio,key=lambda s:s['price'])
print('cheaper = ',cheaper)
expensiver  = heapq.nlargest(3,portfolio,key=lambda s:s['price'])
print('expensiver = ',expensiver)

cheapest = min(portfolio,key=lambda s:s['price'])
print('cheapest = ',cheapest)
expensivest = max(portfolio,key=lambda s:s['price'])
print('expensivest = ',expensivest)

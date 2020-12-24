#怎样找出一个序列中出现次数最多的元素呢？
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
wordsCounter = Counter(words)
topThree = wordsCounter.most_common(3)
print(topThree)
morewords = ['why','are','you','not','looking','in','my','eyes']
a = Counter(morewords)
wordsCounter.update(morewords)
topThree = wordsCounter.most_common(3)
print(topThree)
#Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合。比如：
c = wordsCounter - a
print(c)

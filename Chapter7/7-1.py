#position
def getSum(*args):
    return sum(args)
print(getSum(1,2,3,4))
#named
def getArgs(**args):
    attributes = ['%s="%s"' % item for item in args.items()]
    print(attributes)
getArgs(some=1,big=True)

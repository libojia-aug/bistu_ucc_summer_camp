def maxNum(maxNum=1000):
    a = 0
    b = 1
    while b < maxNum:
        print(b)
        a, b = b, a + b


def maxCount(maxCount=100):
    a = 0
    b = 1
    count = 0
    while count < maxCount:
        print(b)
        a, b = b, a + b
        count = count + 1

maxNum(100)
maxCount(10)

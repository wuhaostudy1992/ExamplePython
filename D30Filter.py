import random
from itertools import compress

blendList = []
for i in range(10):
    if random.randint(0, 3) > 0:
        blendList.append(random.randint(-100, 100))
    else:
        if random.randint(0, 1) == 0:
            blendList.append(random.randint(-100, 100)/10)
        else:
            blendList.append(-random.randint(-100, 100)/10)
print(blendList)

p = (n for n in blendList if n > 0)
print('The below is some positive numbers in the List:')
print(list(p))

p = (n if n>0 else -n for n in blendList)
print('The below is some non-negative numbers in the List:')
print(list(p))

def isInt(val):
    '''try:
        x = int(val)
        return True
    except ValueError:
        return False'''
    if isinstance(val, (int)):
        return True
    return False

'''result = filter(isInt, blendList)
for item in result:
    print(item)'''
print('The below is some integer numbers in the List:')
ivalues = list(filter(isInt, blendList))
print(ivalues)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
    '9',
    '10',
]

more5 = (n>5 for n in blendList)
print(list(compress(addresses, more5)))
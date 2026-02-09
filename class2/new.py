# from module import sInterest,cInterest
# from module import *   (for everything)
# import module as m
# import os
#   print(os.getcwd)
# p=1000
# t=2
# r=12
# print(f'simple interest {sInterest(p,t,r)}')

#streamlit install
#python ko list heterogeneous
# !pip install numpy
#Exceptional handling
try:
    n1=int(input("Enter n1 "))
    n2=int(input("Enter n2 "))
    result=n1/n2
    print(f'the result is {result}')
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print('ENter valid number')
finally:
    print('run')


# from collections import Counter
# nums=[1,2,2,3,3,3]
# c=Counter(nums)
# print(c)
# print(type(c))


# from collections import defaultdict
# aDict=defaultdict(int)
# aDict['a']=aDict['a']+1
# print(aDict)

# from collections import deque
# q=deque([1,2,3,4])
# # q.appendleft(0)
# # q.append(0)

# q.popleft()
# print(q)

# from collections import namedtuple

# Point=namedtuple('Point','x y')
# p=Point(3,4)
# print(p.x,p.y)








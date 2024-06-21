#Method--1
"""Print First 10 natural numbers using while loop

Expected output:

1
2
3
4
5
6
7
8
9
10
"""
def one(x):
    for i in range(1,x+1):
        print(i)
x = int(input())
print(one(x))
#Method--2
a = int(input())
i = 1
while i<=a:
    print(i)
    i+=1


"""Write a program to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
x = int(input())
y = int(input())
for i in range(x,y):
    for j in range(x,i+1):
        print(j,end = " ")
    print()

















        
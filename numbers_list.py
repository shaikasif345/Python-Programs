nums = list(map(int,input("Enter the number to add in a list: ").split(", ")))
for i in nums:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)
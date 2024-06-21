a = input("Enter the sentence: ")
words = a.split()
separated = []
for i in words:
    if len(i)>2:
        separated.append(i)
print(separated)
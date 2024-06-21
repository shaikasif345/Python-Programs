#Write a program to print multiplication table of a given number
#Using For loop
num = int(input("Enter the number to print its table:"))
print(f"Multiplication Table of {num}:")
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
#Using list Comprehension
num = int(input("Enter the number to print its table: "))
multiplication_table = [f"{num} X {i} = {num*i}" for i in range(1,11)]
print("\n".join(multiplication_table))


def palindrome_number(num):
    original_num = num
    reverse_num = 0
    while num > 0:
        remainder = num % 10
        reverse_num = (reverse_num * 10) + remainder
        num = num//10
    if original_num == reverse_num:
        print("The given number is palindromic number")
    else:
        print("The given number is not a palindromic number")
    
num = int(input())
print(palindrome_number(num))
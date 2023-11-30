user_input = int(input("Enter a number: "))
str_number = str(user_input)
if str_number == str_number[::-1]:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
user_list = input("Enter a list of numbers")
number_list = [int(num) for num in user_list.split(',')]
if number_list[0] == number_list[-1]:
    print("The first and last numbers are the same")
else:
    print("The first and last numbers are different")
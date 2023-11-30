user_list_1= input("enter first list of numbers")
user_list_2= input("enter second list of numbers")
list_1= [int(x)for x in user_list_1.split(',')]
list_2= [int(y)for y in user_list_2.split(',')]
result_list=[]
for i in list_1:
    if i%2!=0:
        result_list.append(i)
for j in list_2:
    if j%2==0:
        result_list.append(j)
print(result_list)        
    
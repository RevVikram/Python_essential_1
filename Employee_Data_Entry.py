num_of_employees = input("Enter the Number of Employees")
num = int(num_of_employees)
sum = 0
for i in range(num):
    first_name = input("Enter your first Name:")
    last_name = input("Enter your  Last Name:")
    age_str = input("Enter your Age:")
    age = int(age_str)
    if len(first_name) > 0 and len(last_name) > 0:
        is_between =age in range(18,101)
        print("its working")
        print("The Employee First Name is", first_name)
        print("The Employee Last Name is", last_name)
        print("The Employee Age is", age)
        sum =age +sum
    else:
        print("not valid input")
if sum > 500:
    print("The sum is", sum)
else:
    print("The sum is less than 500")












def employee_name(name_type):
    while True:
        name_var = input(f"enter the {name_type}:")
        if len(name_var.strip()) > 0:
            return name_var
def age_read():
    while True:
        age_str = input("Enter the employee age:")
        if age_str.isdigit():
            age = int(age_str)
            if 18 <=age<= 100:
                return age
            else:
                print("You are not in the right age to be Employed by company")
        else:
            Print("You entered invalid input")
if __name__ == '__main__':
    num_of_employee = int(input("Enter the number of employee:"))
    total_age = 0
    for employee in range(num_of_employee):
        first_name = employee_name("First Name")
        last_name = employee_name("Last Name")
        age = age_read()
        total_age = total_age + age
        print(f"Employee details are:First name:{first_name}, Last name:{last_name}, Age:{age}")
        print(f"Total age: {total_age}")
    if total_age > 500:
        print("total age is exceeded 500")
    else:
        print("total number is less than 500")







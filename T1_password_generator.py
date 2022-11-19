import random

def password_generation():

    list1_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list2_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    password = ""
    position_of_password = random.randint(0, 2)

    lower_quantity = random.randint(3, 5)
    upper_quantity = random.randint(2, 6)
    numbers_quantity = random.randint(3, 5)

    if position_of_password == 0:

        for item in range(0, lower_quantity):
            lower = random.choice(list1_lower)
            password = password + lower

        for item in range(0, upper_quantity):
            upper = random.choice(list2_upper)
            password = password + upper

        for item in range(0, numbers_quantity): 
            numbers = random.randint(0, 9)
            password = password + str(numbers)


    if position_of_password == 1:

        for item in range(0, upper_quantity):
            upper = random.choice(list2_upper)
            password = password + upper

        for item in range(0, lower_quantity):
            lower = random.choice(list1_lower)
            password = password + lower

        for item in range(0, numbers_quantity): 
            numbers = random.randint(0, 9)
            password = password + str(numbers)



    if position_of_password == 2:

        for item in range(0, numbers_quantity): 
            numbers = random.randint(0, 9)
            password = password + str(numbers)

        for item in range(0, upper_quantity):
            upper = random.choice(list2_upper)
            password = password + upper

        for item in range(0, lower_quantity):
            lower = random.choice(list1_lower)
            password = password + lower

    return password



get_process = '0'
password_memory = {}

while get_process != '3':

    print("\n1. Generate Password")
    print("2. Get Password")
    print("3. Exit")

    get_process = input("\n Enter the number of the process you want to perform: ")

    if get_process == '1':
        account = input("\n Enter the name of the account for which the password will be generated: ")
        password_memory[ account ] = password_generation()
        print("\n", account, ":", password_memory[account])

    elif get_process == '2':
        account = input("\n Enter the name of the account you want to get the password for: ")
        if account in password_memory:
            print("\n", account, ":", password_memory[account])
        else:
            print("\n The account entered does not exist")

    elif get_process == '3':
        pass

    else:
        print("\n The number entered is not valid, please enter a valid number")


#print(password_memory)
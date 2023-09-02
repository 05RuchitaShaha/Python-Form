import re

user = {} 
options_s = {}
science_qs = {}
options_m = {}
maths_qs = {}

def register():
    username = input("Enter the name : ")
    #email = input("Enter a valid email-id : ")
    mail()
    #password = input("Enter a valid 8 or 16 digit password : ")
    password = input("Enter the password : ")
    pattern = r'\A(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&8=+])(?!.*\s).{8,16}\Z'
    res = re.findall(pattern, password)                                            
    if res:
        print("This password is valid. ")
        print("\nRegistration Successful !")
    else:
        print("Enter appropriate password, this is invalid. ")
    user[username] = password


def login():
    print("\nLogin and complete the process !")
    username = input("Enter the name : ")
    password = input("Enter a valid 8 or 16 digit password : ")
    if username in user:
        if user[username] == password:
            print("\nLogin Successful ! Now you can create your own quiz.")
            add_qs()
        else:
            print("\nYour password doesn't match the registered ones, enter correct one.")
            login()                        # directly u get the login page without refreshing
    else:
        print("\nYour username is invalid, Enter the registered username.")
        login()                # directly u get the login page without refreshing


def add_qs():
    quiz = input("\nDo you want to set quiz on any of the topics? (y/n) : ")
    if(quiz.lower() == 'y'):
        subject = input("\nEnter the topic of quiz (science/maths) : ")
        level = input("\nEnter the level of difficulty (easy/medium/hard) : ")
        if(subject.lower() == 'science'):
            no_of_qs = int(input("How many questions you want to display ? : "))
            for i in range(no_of_qs):
                qs = input("\nEnter the question. : ")
                opt_s = input("Enter the options separated by space : ")
                options_s[qs] = opt_s
                answers = input("Enter the answer : ")
                science_qs[qs] = answers 
            view_s()

        elif(subject.lower() == 'maths'):
            no_of_qs = int(input("How many questions you want to display ? : "))
            for i in range(no_of_qs):
                qm = input("\nEnter the question. : ")
                opt_m = input("Enter the options separated by space : ")
                options_m[qm] = opt_m
                answerm = input("Enter the answer : ")
                maths_qs[qm] = answerm
            view_m()
        
        else:
            print("Enter valid topic.")
    else:
        print("Exit.") 
    

def view_s():
    view = input("\nDo you want to view the questions? (y/n) : ")
    if(view.lower() == 'y'):
        for i in science_qs.keys():
            print(i)
    else:
        print("Exit")

    opts = input("\nDo you want to view the options? (y/n) : ")
    if(opts.lower() == 'y'):
        for i in options_s.keys():
            print(i)
    else:
        print("Exit")

def view_m():
    view = input("\nDo you want to view the questions? (y/n) : ")
    if(view.lower() == 'y'):
        for i in maths_qs.keys():
            print(i)
    else:
        print("Exit")

    opts = input("\nDo you want to view the options? (y/n) : ")
    if(opts.lower() == 'y'):
        for i in options_m.keys():
            print(i)
    else:
        print("Exit")


def mail():
    email = input('Enter the maid id : ')
    pattern = r'^[\w\.-]+@[a-z]+\.[a-z]{2,5}$'          
    res = re.findall(pattern, email)
    if res:
        print("Your mail id is valid.")
    else:
        print("Enter a valid mail id.")



print("Welcome to the Dashboard ! \nEnter your choice to go further.")
choice = {1:"Press 1 for Registration", 2:"Press 2 for Login"}        # enter the choice here 
for value in choice:
    print('\n', str(value)+'.',choice[value])     # convert to str to print the value of key
choice_input = int(input("Enter the no. : "))
if choice_input == 1:
    register()
elif choice_input == 2:
    login()
else:
    print("Exit")         


print("\nTo register type 1, or to login type 2.")
n = int(input("Enter the number : "))
if n == 1:
    register()
    print("\nTo login type 1 or exit the page")
    a = int(input("enter the response : "))
    if a == 1:
        login()
    else:
        print("Thank You")
elif n == 2:
    login()
else:
    print("Exit")




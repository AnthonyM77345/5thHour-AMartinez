#Name:Anthony Martinez
#Class: 5th Hour
#Assignment: HW12


#1. Print Hello World!
print("Hello World")
#2. Create three different boolean variables named Wi-Fi, login, and admin.
wifi= True
login= True
admin= True
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
boy= 0
#4. Create a nested if statement that checks to see if Wi-Fi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one if they are "missing".
if wifi == True:
    if login == True:
        if admin == True:
             print("login is a go")
             boy += 1
        else:
            print("admin is not a go")
    else:
        print("login is not a go")
else:
    print("wifi is not a go")

# Rules
# At least 8 chars
# Contains number
# Contains special char
# Contains uppercase
# Output
# Strong / Weak + reason
# Concepts
# Strings
# Loops
# Functions
# Logical thinking



def password(x):
    import string
    # x = "tesT@123"

    Uppercase = False
    Lowercase = False
    Number = False
    Special = False
    l = False

    U = string.ascii_uppercase
    L = string.ascii_lowercase
    N = string.digits
    P = string.punctuation

    if len(x) >= 8:
        l = True

    for a in x:
        if a in U:
            Uppercase = True
        elif a in L:
            Lowercase = True
        elif a in N:
            Number = True
        elif a in P:
            Special = True

    if Uppercase == False:
        print("Weak Password :: Please consider atleast one upper case")
    if Lowercase == False:
        print("Weak Password :: Please consider atleast one lower case")
    if Number == False:
        print("Weak Password :: Please consider atleast one Number")
    if Special == False:
        print("Weak Password :: Please consider atleast one special charector")
    if l == False:
        print("Weak Password :: length less than 8 please consider more than 8")

    if Uppercase == True and Lowercase == True and Number == True and Special == True and l == True:
        print("Your password is strong kudos!!")
    return 

x = input("Enter Your Password")    
password(x)
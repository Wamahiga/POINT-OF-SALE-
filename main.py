from customer import *
from product import *
from queries import *

def menu():
    print("**** WELCOME PLEASE INPUT AN OPTION TO PROCEED****")
    print("1. Customer operations")
    print("2. Product operations")
    print("3. Search operations")
    print("4. Quit")

    option=int(input("Choose an option: "))
    if option==1:
        customermenu()
    elif option==2:
        productmenu()
    elif option==3:
        queries()
    elif option==4:
        quit()
    else:
        print("Please enter a valid input")

if __name__ == "__main__":
    menu()

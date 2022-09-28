from product import *
from customer import *
from purchase import *
from queries import *


def menu():
    loop = 1
    while loop:
        print('''*** WELCOME PLEASE INPUT AN OPTION TO PROCEED****
        [1]. Customer Operations
        [2]. Product Operations
        [3]. purchases
        [4]. Queries
        [5]. Exit
        ''')
        option = int(input("Choose One Option:"))
        if option == 1:
            customer_operations()

        elif option == 2:
            product_operations()

        elif option == 3:
            purchase_menu()

        elif option == 4:
            queries()

        elif option == 5:
            loop = 0
            print("exiting application")

        else:
            print("invalid option")


if __name__ == '__main__':
    menu()

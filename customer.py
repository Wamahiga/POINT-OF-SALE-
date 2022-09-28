import random

def customer_operations():
    print("[1]. Add customer")
    print("[2]. Delete customer")
    print("[3]. Update customer")
    print("[4].  Back to Main Menu")

    option = int(input("Choose One Option: "))

    while option:
        if option == 1:
            add_customer()
            break
        elif option == 2:
            delete_customer()
            break
        elif option == 3:
            update_customer()
            break
        elif option == 4:
            from main import menu
            menu()
            break

def add_customer():
    customer_id = random.randint(10000, 100000)
    customer_name = input("ENTER CUSTOMER NAME: ")
    customer_gender = input("WHAT IS YOUR GENDER:")
    customer_phone = input("ENTER CUSTOMER PHONE NUMBER: ")

    z = f'{customer_id},{customer_name},{customer_gender},{customer_phone}\n'

    with open('customer.txt', 'a') as outfile:
        print("Customer Added successfully.")
        outfile.write(z)


def update_customer():
    with open("customer.txt", "r") as s:
        slist = s.readlines()
        customer_id = input("ENTER CUSTOMER ID: ")
        for Line in slist:
            if customer_id in Line:
                line_index = slist.index(Line)

                user_input = input("ENTER NEW PHONE NUMBER: ")
                k = Line.split(',')
                k[2] = user_input
        s = ','
        slist[line_index] = s.join(k)

        with open('customer.txt', 'w') as outfile:
            print("Customer Updated successfully.")
            for Line in slist:
                outfile.write(Line)


def delete_customer():
    with open("customer.txt", "r") as s:
        slist = s.readlines()
        customer_id = input("ENTER CUSTOMER ID: ")
        for Line in slist:
            if customer_id in Line:
                line_index = slist.index(Line)

                slist.pop(line_index)

        with open('customer.txt', 'w') as outfile:
            print("Customer Deleted successfully.")
            for Line in slist:
                outfile.write(Line)

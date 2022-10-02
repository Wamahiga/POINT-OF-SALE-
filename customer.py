import os
customers = []
class Customer:

    def __init__(self, id, gender, name, address):
        

        # instance variables
        self.id = id
        self.gender = gender
        self.name = name
        self.address = address

def customer_operations():
    customer_list = []

    while True:
        print(
            """
            ***CUSTOMER MENU ***
            1.Customer List
            2.Add a new customer
            3.Update a customer
            4.Delete a customer
            5.Search a customer
            0.Back to main menu
            """
        )

        option = int(input("Please input an option to proceed:"))

        if option == 1:
            print()
            list_customers()
        elif option ==2:
            print()
            customer_list.append(create_customer())
            print(customer_list)

        elif option ==3:
            print()
            update_customer()

        elif option == 4:
            print()
            delete_customer()
        
        elif option == 5:
            search_customer()

        elif option == 0:
            print()
            break

        else:
            print()
            print('Invalid option')

##option 1 list customer function

def list_customers():
    customers = []
    customer_list =[]
    with open('customer.txt','r') as reader:
        for line in reader.readlines():
            customers.append(line)

    for n in customers:
        lists = n.replace('\n', '')
        customer_list.append(lists)
    print(customer_list)


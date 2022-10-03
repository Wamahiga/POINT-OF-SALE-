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

        option = int(input("Please input an option to proceed:  "))

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
            print('Invalid option!,Please try again')

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

def create_customer():

    f = open('customer.txt','a+', newline='')

    customer_id = input("Enter customer id : ")
    with open("customer.txt", 'r') as f_r:

        for line in f_r.readlines():
            element_list = []
            line_data = line.split(',')
            element_list.append(line_data[0])

            if customer_id in element_list:
                print()
                print("user id exists! enter a different id")
                return create_customer()

    
    customer_name = input("Enter Customer name:  ").lower()
    customer_gender= input("What is the customer's gender: ").lower()
    address = input("Enter customer address:   ")
    f.write(customer_id + ',' +customer_gender + ',' +  customer_name  +  ','  +  address + "\n")
    f.close()
    if(f):
        print("New Customer added successfully!!!")
    print()
    output = {"id": customer_id, "gender": customer_gender, "name": customer_name, "address": address}
    return output


def update_customer():
    file = open('customer.txt', 'r')
    temp = open('temp.txt', 'w')
    id = int(input("Enter customer id"))
    uf = " "
    while(uf):
        uf = file.readline()
        s = uf.split(",")
        if len(uf)>0:
            if int(s[0])==id:
                name = input("Enter Customer name: ").lower()
                gender = input("what is the customers gender?")
                address = input("enter customer address: ")
                temp.write(str(id) + ',' + name + ',' + gender + ',' + address + "\n")
            else:
                temp.write(uf)
    temp.close()
    file.close()
    os.remove('customer.txt')
    os.rename('temp.txt','customer.txt')
    print("CUSTOMER UPDATED SUCCESFULLY!!!")
    list_customers

    ##error handling

def delete_customer():
    customer = open("customer.txt", 'r')
    temp =open("temp.txt", 'w')
    id = int(input("Enter customer id to delete: "))
    df= ' '
    while(df):
        df = customer.readline()
        s = df.split(',')
        if len(df)>0:
            if int(s[0]) !=id:
                temp.write(df)

    customer.close()
    temp.close()
    os.remove('customer.txt')
    os.rename('temp.txt','customer.txt')
    print("Customer is deleted successfuly! ")
    list_customers()


def search_customer():
    customer = open('customer.txt','r')
    id = int(input("Enter customer id:  "))
    print()
    s = ' '
    while(s):
        s = customer.readline()
        L = s.split(",")
        if len(s)>0:
            if int(L[0]) == id:
                print("************CUSTOMER DETAILS****************")
                print("Customer id: ",L[0])
                print("Customer Name: ",L[1])
                print("Customer Address: ",L[2])



def show_customers():
    file = open('customer.txt','r')
    for i in file:
        item = i.split(',')
        id = item[0]
        name = item[1]
        address = item[2]
        customer = Customer(id,name,address)
        customers.append(customer)
        







    if __name__ == "__main__":
        customer_operations()





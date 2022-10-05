import os
import customer, product

PRODUCTS = []
CUSTOMERS = []
PURCHASES = []

def purchase_menu():
    

    # creating purchase options  
    while True:
        print("""
        Purchases Menu
        1. View all items
        2. Make a Purchase
        3. search for an item
        0. Back to main menu
        """)  
        option = int(input("Select Purchase option:"))  

        # choice 1
        if option == 1:
            print()
            list_purchase()
            
        elif option == 2:
            print()
            make_purchase()
        elif option == 3:
            print()
            search_purchase()
        elif option == 0:
            print()
            break
        else:
            print()
            print('Incorrect choice. Please try again! ')

class Purchase:

    def __init__(self,customer_name, product_id, purchase_item, price_purchased):
        assert purchase_item >=0, f'{purchase_item} is not greater or equal to zero!'

        self.customer_name = customer_name
        self.product_id = product_id
        self.purchase_item = purchase_item
        self.price_purchased = price_purchased

        def __repr__(self):
            return f"('{self. customer.name}', '{self.product_id}','{self.purchase_item}', '{self.price_purchased}')"





    





def list_purchase():
    purchases = []
    purchase_list = []
    with open('purchase.txt', 'r') as reader:
        for line in reader.readlines():
            purchases.append(line)

    for p in purchases:
        list = p.replace('\n','')
        purchase_list.append(list)
    print(purchase_list)



# function to make a purchse

def make_purchase():
    customer.show_customers()
    product.show_products()
   
    customer_exists = False
    product_exists = False
    cus_id = input("Enter customer id : ")
    # check if the customer id exists
    for cus in customer.customers:
        if cus_id == cus.id:
            customer_exists = True
            cus_name = cus.name
            print("Customer name is:  " , cus_name)
            break
           

    
    # check if product exists
    pro_id = input("Enter product id to purchase: ") 
    for prod in product.PRODUCTS:
        if pro_id ==prod.id:
            product_exists = True
           
      
    if customer_exists and product_exists:

        # make purchase
        purchase_q = int(input("Enter quantity of product to purchase: "))

# checking if product is available

 # update product 

 # search for product

                    
# calculate the total spent on a product

# calculating total spent by the customer                  









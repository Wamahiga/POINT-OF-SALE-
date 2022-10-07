import os
import customer, product

PRODUCTS = []
CUSTOMERS = []
PURCHASES = []

def purchase_menu():
    

    # creating purchase options  
    while True:
        print("""
        ****PURCHASE MENU****
        [1]. List all purchases
        [2]. Make a Purchase
        [3]. Find a purchase
        [0]. Back to main menu
        """)  
        option = int(input("Select Purchase option:"))  

        # choice 1
        if option == 1:
            print()
            list_purchase()
            
        elif option == 2:
            print()
            make_purchases()
        elif option == 3:
            print()
            find_purchase()
        elif option == 0:
            print()
            break
        else:
            print()
            print('Invalid option. Please try again! ')

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



# function to make a purchAse

def make_purchases():
    customer.show_customers()
    product.show_products()
   
    customer_exists = False
    product_exists = False
    cus_id = input("Enter customer id to purchase: ")

    # check if the customer exists
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
        purchase_quantity = int(input("Enter quantity of product to purchase: "))

        # checking if product amount is available
        for i in range(len(product.PRODUCTS)):
            if pro_id == product.PRODUCTS[i].id:
                name = product.PRODUCTS[i].name
                quantity = int(product.PRODUCTS[i].quantity)
                if quantity >= purchase_quantity:
                    # update product amount
                    balance = quantity - purchase_quantity
                   
                    price = float(product.PRODUCTS[i].price)
                    price_purchased = price * purchase_quantity
                    output = Purchase(cus_name,pro_id,purchase_quantity,price_purchased)
                    PURCHASES.append(output)
                    print("Product Purchase successfull!!!")
                    
                    
                    # update_products()
                    while True:
                        print ("""
                        **CHOOSE AN OPTION TO CONTINUE **
                        [1]. Make another purchase
                        [2]. Checkout
                        [3]. Exit
                        """)
                        option = int(input("Choose a purchase option: "))
                        if option ==1:
                            make_purchases()
                        elif option ==2:
                            checkout()
                            break
                        elif option ==3:
                            print()
                            break

                        else:
                            print("Invalid option!!!")
                        
                else:
                    print("Quantity in stock is below " +str(purchase_quantity) + ' : ' +"quantity available:"+str(quantity) )
                    make_purchases()
                    break
  
    else:
        print("Records not found ,please update and try again")






def checkout():
    total_purchase = 0
    for pur in PURCHASES:
        cost = float(pur.price_purchased)
        total_purchase += cost
        print()
        print("Total: "+ str(total_purchase))
        print("Purchase complete.")
        update_products()
        handle_file()

 


def update_products():
    for pur in PURCHASES:
        product_id = pur.product_id
        pur_quantity = int(pur.purchase_item)
        file = open('product.txt', 'r')
        temp = open('temp.txt', 'w')
        s = ' '
        while(s):
            s = file.readline()
            L = s.split(',')
            if len(s)> 0:
                if (L[0]) == product_id:
                    name = L[1]
                    quantity = int(L[2])
                    price = L[3]
                    updated_quantity = quantity - pur_quantity
                    temp.write(str(product_id) + ',' + name + ',' + str(updated_quantity) + ',' + str(price))
                    
                else:
                    temp.write(s)
        temp.close()
        file.close()
        os.remove('product.txt')
        os.rename('temp.txt', 'product.txt')
        print("Inventory is updated.")
        print("Stock remaining for " + name + ' : ' + str(updated_quantity))

def handle_file():
    with open('purchase.txt', 'a') as fo:
        for pur in PURCHASES:
            print(pur.customer_name + ',' + pur.product_id + ',' +str(pur.purchase_item) + ',' + str(pur.price_purchased), file=fo)

  

def find_purchase():
    total = 0
    items_bought = 0

    # seach purchase menu

    while True:
        print("""
       *****  Search Options: *****
        [1]. Search by Customer name
        [2]. Search by Product Id
        [0]. Back to main menu
        """)

        option = int(input("Select search option: "))
        if option ==1:
            fo = open('purchase.txt', 'r')
            customer_name = input("Please enter the customer name: ").lower()
            s = ' '

            while(s):
                s = fo.readline()
                L = s.split(',')
                if len(s)>0:
                    if(L[0]) == customer_name:
                        product_id = L[1]
                        quantity = L[2]
                        price = float(L[3])
                        print( )
                        # calculating total spent by the customer
                        total += price
                        print("Customer name: ", customer_name)
                        print("Product id: ", product_id)
                        print("Quantity purchase: ", quantity)
                        print("Price: ", price)

            print('*************')
            print("Total spent by " + customer_name + ' : ' + str(total))
            break

        elif option == 2:
            fo = open('purchase.txt', 'r')
            id = input("Please enter a product_id: ")

            s = ' '
            while(s):
                s = fo.readline()
                L =s.split(',')
                if len(s)>0:
                    if(L[0]) == id:
                        customer_name = L[0]
                        quantity = int(L[2])
                        price = float(L[3])
                        print( )

                        # calculate the total spent on a single product

                        total += price
                        items_bought += quantity
                        print("Customer name: ", customer_name)
                        print(" Quantity purchased: ", quantity)
                        print("Price: ", price)

            print('**************')
            print("Total spent: " + str(total))
            print()
            print("products purchased: " + str(items_bought))
        
        elif option == 0:
            print()
            break

        else:
            print()
            print("Sorry! Invalid option. Please try again.")


    
    if __name__ == "__main__":
        purchase_menu() 










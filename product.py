import os
PRODUCTS = []

# product class
class Product:
    def __init__(self,id,name,quantity,price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price =price



def product_operations():
    product_list = []

    while True:
        print("""
        *******PRODUCT MENU*******
        1. Product List
        2. Create a product
        3. Update a product
        4. Delete a product
        5. Search a product
        0. Back to main menu
        """)

        option = int(input("Choose a product option: "))

        if option == 1:
            print()
            list_products()
        elif option ==2:
            print()
            product_list.append(create_product())
            print(product_list)

        elif option ==3:
            print()
            update_product()

        elif option == 4:
            print()
            delete_product()

        elif option == 5:
            search_product()

        elif option == 0:
            print()
            break

        else:
            print()
            print('invalid option')

def list_products():
    products = []
    products_list = []
    with open('product.txt','r') as reader:
        for line in reader.readlines():
            products.append(line)
   
    for p in products:
        lists = p.replace('\n','')
        products_list.append(lists)
    print(products_list)


def create_product():
    f = open('product.txt', 'a+', newline='')

    product_id = input("Enter new Product id : ")
    with open("product.txt",'r') as f_r:
        for line in f_r.readlines():
            element_list =[]
            line_data = line.split(',')
            element_list.append(line_data[0])

            
            if product_id in line:
                print()
                print("The ID already exists!! Enter a a different ID !!")
                print()
                return create_product()

    product_name = input("Enter the name of the Product:  ").lower()
    quantity = input("Enter the quantity of the product:   ")
    price = input("Enter the price of the product:   ")
    f.write(product_id + ',' +  product_name  +  ','  +  quantity + ',' + price + "\n")
    f.close()
    if(f):
        print("Product added successfully!!!")
    print()
    output = {"id": product_id, "name": product_name, "quantity": quantity, "price": price}
    return output

def update_product():
    file = open('product.txt','r')
    temp = open('temp.txt','w')
    id = input("Enter Product id: ")
    uf = ' '
    while(uf):
        uf = file.readline()
        s = uf.split(',')
        if len(uf)>0:
            if s[0] == id:
                name = input("Enter Product name: ")
                quantity = int(input("Enter product quantity : "))
                
                price = int(input("Enter the product price : "))
               
                temp.write(str(id) + ',' +  name  +  ','  +  str(quantity) + ',' + str(price) + "\n")
            else:
                temp.write(uf)
    temp.close()
    file.close()
    os.remove('product.txt')
    os.rename('temp.txt','product.txt')
    print("Product updated successfuly!!")
    list_products()




def delete_product():
    product= open("product.txt", 'r')
    temp =open("temp.txt", 'w')
    id = int(input("Enter product id to delete: "))
    df = ' '
    while(df):
        df= product.readline()
        s = df.split(',')
        if len(df)>0:
            if int(s[0]) !=id:
                temp.write(df)

    product.close()
    temp.close()
    os.remove('product.txt')
    os.rename('temp.txt','product.txt')
    print("Product is deleted successfuly! ")
    list_products()



def search_product():
    product = open('product.txt','r')
    id = input("Enter product id to search:  ")
    print()
    s = ' '
    while(s):
        s = product.readline()
        L = s.split(",")
        if len(s)>0:  
            if L[0] == id:

                print("**********product details****************")
                print("Product id: ",L[0])
                print("Product Name: ",L[1])
                print("Product amount: ",L[2])
                print("Product price: ",L[3])

def show_products():
    product = open("product.txt","r")
    for p in product:
        try:
            prod = p.split(',')
            id = prod[0]
            name = prod[1]
            quantity = int(prod[2])
            price = prod[3]
            output = Product(id,name,quantity,price)
            PRODUCTS.append(output)
        except:
            print()
    





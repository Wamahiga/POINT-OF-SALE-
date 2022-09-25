
def productmenu():
    print("**** PRODUCT OPERATIONS ****")
    print("1. Add a new product")
    print("2. Delete a product")
    print("3. Update a product")
    print("4. Goback to main menu")

    option=int(input("Choose an option: "))
    if option==1:
        print("insert a new product to record:")
        addproduct()
        productmenu()
    elif option==2:
        print("Delete a product from the record")
        deleteproduct()
        productmenu()
    elif option==3:
        print("Update an existing product")
        updateproduct()
        productmenu()
    elif option==4:
        from main import main
        main()
    else:
        print("Please enter a valid input")
        productmenu()

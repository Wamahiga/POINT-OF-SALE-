
def customermenu():
    print("**** PRODUCT OPERATIONS ****")
    print("1. Add a new customer")
    print("2. Delete a customer record")
    print("3. Update a customer")
    print("4. Goback to main menu")

    option=int(input("Choose an option: "))
    if option==1:
        print("insert a new customer to record:")
        addcustomer()
        customermenu()
    elif option==2:
        print("delete a customer from the records")
        deletecustomer()
        customermenu()
    elif option==3:
        print("Update an existing customer's details")
        updatecustomer()
        customermenu()

    elif option==4:
       quit()
    else:
        print("Please enter a valid input")
    customermenu()

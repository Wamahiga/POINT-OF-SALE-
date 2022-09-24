def main():
   while True:
        print('''
                ----Main menu----
                1. Customer Operations 
                2. Product OPerations 
                3. Purchase operation 
                4. Queries 
                5. Exit
        ''')

        option= int(input("choose one of the options below"))
        if option == 1:
            customeroperations()

        elif option == 2:
            productoperations()
        
        elif option == 3:
            queries()
        
        elif option == 4:
            quit()

        elif option == 6:
            print("select a valid option ")

if __name__ == '__main__':
    menu()

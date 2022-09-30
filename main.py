from classes import node
from classes import contact
from classes import Contact_list

def main():
    

    contact_lst = Contact_list()

    while True:
        
        selection = input("Enter 1 to add a new contact \nEnter 2 to see all contacts on the list \nEnter 3 to remove a name and number of the name \nEnter 4 to change a number \nEnter 5 to exit \nYour answer is: ")
        if selection == "1":
            name = input("Enter name: ")
            number = input("Enter number: ")
            contact_lst.add(name, number)
            

        elif selection == "2":
            print(contact_lst)
            
        
        elif selection == "3":
            name = input("Enter name: ")
            contact_lst.remove_name(name)
        
        elif selection == "4":
            name = input("Enter name: ")
            number = input("Enter number: ")
            contact_lst.change_phone_number(name, number)
        
        elif selection == "5":
            break
        else:
            print("Invalid input")

main()
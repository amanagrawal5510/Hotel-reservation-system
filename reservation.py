from database import Database
from menu import User
from menu import update, check, availability

Database.initialize(database='learning', host='localhost', user='postgres', password='211409')


def reservation():
    user_input = input("What can I do for you?") # (a for add guest, l to load details, u to update after check_out, c to get amount, o to quit)

    while user_input != 'q':
        if user_input == 'a':
            cus_name = input("Enter your name: ")
            cus_room = input("Select the room you want: ")
            if cus_room not in ['Presidential', 'Suite', 'Double', "Standard"]:
                print("Wrong Room")
            else:
                availability(cus_room)
            ch_in = input("Enter check-in date (YYYY-MM-DD): ")
            ch_out = input("Enter check-out date (YYYY-MM-DD): ")
            cust_new = User(cus_name, cus_room, ch_in, ch_out)
            cust_new.insert_to_db()

        elif user_input == 'l':
            cus_name = input("Enter your name: ")
            cus_details = User.load_from_db(cus_name)
            print(cus_details)

        elif user_input == 'u':
            cus_name = input("Enter customer's name: ")
            update(cus_name)

        elif user_input == 'c':
            cus_name = input("Enter customer's name: ")
            net = check(cus_name)
            print(net)

        elif user_input == 'o':
            break


reservation()

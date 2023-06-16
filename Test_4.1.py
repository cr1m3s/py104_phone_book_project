4.1 interface 

phone_book = PhoneBook()

while True:

    print("\n-- Main Menu --")

    print("1. Add Contact")

    print("2. Remove Contact")

    print("3. Edit Contact")

    print("4. Search Contact")

    print("5. Exit")

    option = input("Enter option number: ")

    if option == "1":

        phone_number = input("Enter phone number: ")

        name = input("Enter name: ")

        surname = input("Enter surname (optional): ")

        locality = input("Enter locality (optional): ")

        email = input("Enter email (optional): ")

        social_media = input("Enter social media (optional): ")

        contact = Contact

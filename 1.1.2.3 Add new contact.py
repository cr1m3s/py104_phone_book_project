1.1.2.3 Add new contact. If contact exist give user options:

- remove old one and create new one

- edit contact

- or cancel creation of new contact



class Contact:

    def __init__(self, phone_number, name, surname=None, locality=None, email=None, social_media=None):

        self.phone_number = phone_number

        self.name = name

        self.surname = surname

        self.locality = locality

        self.email = email

        self.social_media = social_media

class PhoneBook:

    def __init__(self):

        self.contacts = []

    def add_contact(self, contact):

        existing_contact = self.search_contact(contact.phone_number)

        if existing_contact:

            # Contact already exists, give user options

            print("Contact already exists. Choose an option:")

            print("1. Remove old contact and create new one")

            print("2. Edit contact")

            print("3. Cancel creation of new contact")

            option = input("Enter option number: ")

            if option == "1":

                self.remove_contact(existing_contact.phone_number)

                self.contacts.append(contact)

                print("New contact was added successfully.")

            elif option == "2":

                self.edit_contact(existing_contact.phone_number, contact)

                print("Contact was edited successfully.")

            else:

                print("Creation of the new contact was cancelled.")

        else:

            self.contacts.append(contact)

            print("Contact added successfully.")

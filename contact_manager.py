class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {'name': name, 'phone': phone, 'email': email}
        self.contacts.append(contact)
        print(f"Contact added: {contact}")

    def edit_contact(self, index, name, phone, email):
        if 0 <= index < len(self.contacts):
            self.contacts[index]['name'] = name
            self.contacts[index]['phone'] = phone
            self.contacts[index]['email'] = email
            print(f"Contact edited: {self.contacts[index]}")
        else:
            print("Invalid contact index")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            deleted_contact = self.contacts.pop(index)
            print(f"Contact deleted: {deleted_contact}")
        else:
            print("Invalid contact index")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts):
                print(f"{i+1}. {contact}")

contact_manager = ContactManager()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        contact_manager.add_contact(name, phone, email)
    elif choice == '2':
        index = int(input("Enter the index of the contact to edit: ")) - 1
        name = input("Enter new contact name: ")
        phone = input("Enter new contact phone number: ")
        email = input("Enter new contact email: ")
        contact_manager.edit_contact(index, name, phone, email)
    elif choice == '3':
        index = int(input("Enter the index of the contact to delete: ")) - 1
        contact_manager.delete_contact(index)
    elif choice == '4':
        contact_manager.display_contacts()
    elif choice == '5':
        print("Exiting the Contact Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
 
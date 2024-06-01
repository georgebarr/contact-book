import os
from database import create_contact, view_contact_information, remove_contact
from classes import Contact

CLEAR = ('cls' if os.name == 'nt' else 'clear')

print("Welcome to your contact book.")

user_input = input("Would you like to (C)reate a contact, (V)iew the information of a specific contact or (R)emove a contact?: ").lower().strip()

os.system(CLEAR)


if user_input in ["c", "v", "r"]:


	forename = input("The contact's forename: ")
	surname = input("The contact's surname: ")
	address = input("The contact's address: ")
	phone_num = input("The contact's phone number: ")
	email = input("The contact's email: ")

	contact = Contact(forename, surname, address, phone_num, email)

	if user_input == "c": 

		create_contact(contact)

		print("{} has been added to your contact book!".format(forename + " " + surname)) 

	elif user_input == "v":

		if view_contact_information(contact) == []:

			print("This user is not in your contacts.")

		else: 

			print(view_contact_information(contact))

	elif user_input == "r":

		remove_contact(contact)

		print("Contact deleted.")

else:

	print("Invalid input. Relaunch program.")

	raise SystemExit() 


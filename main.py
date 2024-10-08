import os
from database import create_contact, view_contact_information, remove_contact, all_contact_information
from classes import Contact


print("Welcome to your contact book.")

user_input = input("Would you like to (C)reate a contact, (V)iew the information of a specific contact, (Vi)ew all contacts, or (R)emove a contact?: ").lower().strip()

# Clears the screen for a better user experience.
os.system('cls' if os.name == 'nt' else 'clear')

if user_input == "c": 

	forename = input("The contact's forename: ")
	surname = input("The contact's surname: ")
	address = input("The contact's address: ")
	phone_num = input("The contact's phone number: ")
	email = input("The contact's email: ")

	# Saves the new contact as an object of the Contact class.
	contact = Contact(forename, surname, address, phone_num, email)

	# Adds the new contact to the database.
	create_contact(contact)

	print("{} has been added to your contact book!".format(forename + " " + surname)) 

elif user_input == "vi":

	if all_contact_information() != []:

		# Prints every contact within the database
		for i in all_contact_information(): 
			print(i)

	else:

		print("You currently have no contacts!")

elif user_input == "v":

	surname = input("The contact's surname: ")

	# Creates a new object of the Contact class containing the surname of the person(s) being searched.
	contact = Contact("", surname, "", "", "")

	if view_contact_information(contact) == []:

		print("This person is not in your contacts.")

	else: 

		# Prints out every person which has the same surname as the one being searched.
		for i in view_contact_information(contact): print(i)


elif user_input == "r":

	forename = input("The contact's forename: ")
	surname = input("The contact's surname: ")

	# Creates a new object of the Contact class containing the forename and surname of the person being deleted.
	contact = Contact(forename, surname, "", "", "")

	# Deletes the contact from the database.
	remove_contact(contact)

	print("Contact deleted.")

else:

	print("Invalid input. Relaunch program.")


import sqlite3

con = sqlite3.connect("contacts.db")

cur = con.cursor()

#cur.execute("CREATE TABLE contacts(forename text, surname text, address text, phone text, email text)")

def create_contact(contact):

	"""
    Inserts a contact into the database

    Args:
    	contact (Contact): An instance of the Contact class  
    """

	with con: 

		cur.execute("INSERT INTO contacts VALUES(:forename, :surname, :address, :phone, :email)",
			{"forename": contact.forename, "surname": contact.surname, "address": contact.address,
			"phone": contact.phone, "email": contact.email})


def view_contact_information(contact):

	"""
    Returns the information of a specific contact within the database

    Args:
    	contact (Contact): An instance of the Contact class  
    """

	cur.execute("SELECT * FROM contacts WHERE surname=:surname", {'surname': contact.surname})


	return cur.fetchall()


def update_data(old_value, new_value, option):

	"""
	Allows the user to update a contact's phone or email.

	Args:
		old_value (str): The contact's current information which they would like to change
		new_value (str): What the contact's new information should be
		option (str): Either phone or email, determines what is updated.
	"""

	data = {
		"new_value": new_value,
		"old_value": old_value
		}

	if option == "phone":

		cur.execute("UPDATE contacts SET phone = :new_value WHERE phone = :old_value", 
			data)

	else:

		cur.execute("UPDATE contacts SET email = :new_value WHERE email = :old_value", 
			data)


def remove_contact(contact):

	"""
    Removes a contact from the database

    Args:
		contact (Contact): An instance of the Contact class  
   	"""

	with con: 

		cur.execute("DELETE FROM contacts WHERE forename = :forename AND surname = :surname", 
			{"forename": contact.forename, "surname": contact.surname})


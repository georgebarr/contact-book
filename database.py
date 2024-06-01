import sqlite3

con = sqlite3.connect("contacts.db")

cur = con.cursor()

cur.execute("CREATE TABLE contacts(forename text, surname text, address text, phone text, email text)")

def create_contact(contact):

	"""
    Inserts a contact into the database

    Args:
    contact (Contact): An instance of the contact class  
    """

	with con: 

		cur.execute("INSERT INTO contacts VALUES(:forename, :surname, :address, :phone, :email)",
			{"forename": contact.forename, "surname": contact.surname, "address": contact.address,
			"phone": contact.phone, "email": contact.email})


def view_contact_information(contact):

	"""
    Returns the information of a specific contact within the database

    Args:
    contact (Contact): An instance of the contact class  
    """

	cur.execute("SELECT * FROM contacts WHERE surname=:surname", {'surname': contact.surname})


	return cur.fetchall()


def remove_contact(contact):

	"""
    Removes a contact from the database

    Args:
	contact (Contact): An instance of the contact class  
   	"""

	with con: 

		cur.execute("DELETE FROM contacts WHERE forename = :forename AND surname = :surname", 
			{"forename": contact.forename, "surname": contact.surname})


con.close()
class Contact ():

	"""Stores the contact information for an individual."""

	def __init__(self, fname, sname, address, phone, email):

		"""
        Initializes a new Contact object.

        Args:
            fname (str): The contact's first name.
            sname (str): The contact's last name.
            address (str): The contact's address.
            phone (str): The contact's phone number.
            email (str): The contact's email address.
        """

		self.forename = fname 
		self.surname = sname 
		self.address = address
		self.phone = phone 
		self.email = email 
# data_processor.py
from .utils import validate_email

"""
Contains the DataProcessor class which has methods for processing data and checking the validity of email addresses using the function from utils.py. 

The DataProcessor class offers:
- A method to process data by converting each item in a given list to uppercase.
- A method to check the validity of email addresses provided in a list.
"""

class DataProcessor:
    def process_data(self, data):
        """
        Processes a list of data items by converting each item to uppercase.

        Parameters:
        - data (list): A list of data items (strings).

        Returns:
        - list: A new list containing the uppercase versions of the items from the input list.
        """
        return [item.upper() for item in data]
    
    def check_emails(self, emails):
        """
        Checks a list of emails for validity using a specific pattern to match valid email addresses.

        An email is considered valid if it matches the following criteria:
        - Starts with one or more lowercase letters or digits.
        - An optional dot (.) or underscore (_) can follow the initial characters.
        - Must contain an '@' symbol followed by one or more word characters and a dot.
        - Ends with one or more word characters.

        Parameters:
        - emails (list): A list of email addresses (strings) to be validated.

        Returns:
        - list: A list of boolean values where False represents a valid email address and
          True represents an invalid email address, corresponding to each email in the input list.
        """
        return [validate_email(email) for email in emails]
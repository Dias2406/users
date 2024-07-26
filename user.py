# user.py
import uuid
from .utils.utils import validate_email
"""
Contains the User class which uses the uuid library to generate unique user IDs.
"""
class User:
    def __init__(self, name, email):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
    
    def __str__(self):
        return f"User [ID: {self.id}, Name: {self.name}, Email: {self.email}]"
    
    def update_email(self, new_email):
        if validate_email(new_email):
            raise ValueError("Invalid email format")
        self.email = new_email

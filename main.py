# main.py
"""
The main script that creates a User instance and processes some data using the DataProcessor class.
"""
from user import User
from data_processor import DataProcessor

def main():
    user = User("John Doe", "john.doe@example.com")
    print(user)
    
    processor = DataProcessor()
    data = ["apple", "banana", "cherry"]
    processed_data = processor.process_data(data)
    check_emails = processor.check_emails(["dias@gmail.com", "diasgmail.com"])
    user.update_email("invalid_email")
    print(f"Check Email: {check_emails}")
    print(f"Processed Data: {processed_data}")

if __name__ == "__main__":
    main()

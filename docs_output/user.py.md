# user.py

## ClassDef User

The function of the class is to represent a user with a unique ID, name, and email address.

**Attributes**:

- `id` (`uuid.UUID`): A unique identifier for the user, generated using the `uuid` library.
- `name` (`str`): The name of the user.
- `email` (`str`): The email address of the user.

**Functions**:

- `__init__(self, name, email)` -> `None`
    - Parameters:
        - `name` (`str`): The name of the user.
        - `email` (`str`): The email address of the user.
    - Returns:
        - `None`: This method initializes a new `User` instance.

- `__str__(self)` -> `str`
    - Returns:
        - `str`: A string representation of the `User` instance, including its ID, name, and email address.

- `update_email(self, new_email)` -> `None`
    - Parameters:
        - `new_email` (`str`): The new email address for the user.
    - Returns:
        - `None`: This method updates the email address of the `User` instance.

**Code Description**: The `User` class is designed to encapsulate the details of a user, including a unique identifier (ID), name, and email address. It uses the `uuid` library to generate a unique ID for each instance, ensuring that each user can be uniquely identified. The class provides a method to update the user's email address, allowing for changes to user information after instantiation.

**Note**: The unique ID generated for each user instance ensures that even users with identical names and email addresses can be distinguished.

**Input Example**: 

```
user1 = User("John Doe", "john.doe@example.com")
```
This example creates a new `User` instance with the name "John Doe" and the email address "john.doe@example.com".

**Output Example**:

```
print(user1)
```
This would output something similar to:
```
User [ID: 123e4567-e89b-12d3-a456-426614174000, Name: John Doe, Email: john.doe@example.com]
```
This output shows the string representation of the `User` instance, including its unique ID, name, and email address.
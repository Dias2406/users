# user.py

## ClassDef User

The function of the class is to represent a user with a unique ID, name, and email address.

**Attributes**:

- `id` (`UUID`): A unique identifier for the user, generated using the uuid library.
- `name` (`str`): The name of the user.
- `email` (`str`): The email address of the user.

**Functions**:

- `__init__`(self, `name`: `str`, `email`: `str`) -> `None`
    - Parameters:
        - `name` (`str`): The name of the user.
        - `email` (`str`): The email address of the user.
    - Returns:
        - `None`: This method initializes a new User instance.

- `__str__`(self) -> `str`
    - Returns:
        - `str`: A string representation of the User instance.

- `update_email`(self, `new_email`: `str`) -> `None`
    - Parameters:
        - `new_email` (`str`): The new email address for the user.
    - Returns:
        - `None`: This method updates the email address of the User instance.

**Code Description**: The `User` class uses the `uuid` library to generate a unique identifier for each user instance upon creation. It provides a method to update the user's email address. The `__str__` method allows for a readable string representation of the user, including their unique ID, name, and email address.

**Note**: It's important to ensure that the email address provided is valid and in the correct format before updating it to avoid potential issues.

**Input Example**: 

```
user1 = User("John Doe", "john.doe@example.com")
```
This example creates a new User instance with the name "John Doe" and the email address "john.doe@example.com".

**Output Example**:

```
User [ID: 123e4567-e89b-12d3-a456-426614174000, Name: John Doe, Email: john.doe@example.com]
```
This output is a string representation of the User instance, showing the unique ID, name, and email address of the user.
# user.py

## ClassDef User

The function of the class is to represent a user with a unique ID, name, and email address.

**Attributes**:

- `id` (`UUID`): A unique identifier for the user, generated using the `uuid` library.
- `name` (`str`): The name of the user.
- `email` (`str`): The email address of the user.

**Functions**:

- `__init__`(`name`: `str`, `email`: `str`)
    - Parameters:
        - `name` (`str`): The name of the user.
        - `email` (`str`): The email address of the user.
    - Initializes a new `User` instance with a unique ID, name, and email address.

- `__str__`() -> `str`
    - Returns:
        - `str`: A string representation of the `User` instance, including its ID, name, and email address.

- `update_email`(`new_email`: `str`)
    - Parameters:
        - `new_email` (`str`): The new email address for the user.
    - Updates the email address of the `User` instance.

**Code Description**: This class utilizes the `uuid` library to generate a unique identifier for each user instance upon creation. It provides basic functionalities to access and modify the user's information, such as updating the email address. The `__str__` method allows for a readable representation of the user's details.

**Note**: The unique ID generated for each user instance ensures that every user can be uniquely identified, which is crucial for systems requiring user management.

**Input Example**: 

```
user1 = User("John Doe", "john.doe@example.com")
```
This example creates a new `User` instance with the name "John Doe" and the email address "john.doe@example.com".

**Output Example**:

```
print(user1)
```
This will output: `User [ID: <unique_id>, Name: John Doe, Email: john.doe@example.com]`, where `<unique_id>` is the unique identifier generated for this user instance.
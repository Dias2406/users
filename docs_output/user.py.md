## Updated Documentation

### ClassDef User

The `User` class is designed to model a user within a system, uniquely identified by an ID, and characterized by a name and an email address.

**Attributes**:

- `id` (`UUID`): A unique identifier for the user, automatically generated upon instance creation using the `uuid` library. This ensures that each user has a distinct ID.
- `name` (`str`): The user's name. This attribute represents the full name of the user as a string.
- `email` (`str`): The user's email address. It stores the email contact information for the user.

**Methods**:

- `__init__(self, name: str, email: str) -> None`
    - Initializes a new instance of the `User` class.
    - **Parameters**:
        - `name` (`str`): The name of the user. It should be a valid string representing the user's full name.
        - `email` (`str`): The email address of the user. It should be a valid string representing the user's email address.
    - **Returns**:
        - `None`: This constructor method does not return any value. It simply initializes the `User` object with the provided name, email, and a unique ID.

- `__str__(self) -> str`
    - Provides a string representation of the `User` instance, including the unique ID, name, and email.
    - **Returns**:
        - `str`: A formatted string that includes the user's ID, name, and email address, making it easy to print and identify the user object.

- `update_email(self, new_email: str) -> None`
    - Updates the email address of the user if the new email is valid.
    - **Parameters**:
        - `new_email` (`str`): The new email address to be set for the user. Before updating, it validates the new email address to ensure it's in a proper format.
    - **Returns**:
        - `None`: This method does not return any value. If the new email address is valid, it updates the `email` attribute of the `User` instance, else it remains unchanged.

**Code Description**: The updated `User` class continues to encapsulate user-related data within a system, providing a structured way to manage user information. It leverages the `uuid` library for unique identifier assignment and introduces email validation before updating a user's email, enhancing data integrity and ensuring the email format validity. The validation is performed using the `validate_email` function imported from the `utils` module, which represents a significant enhancement to ensure the correctness of the user's data.

**Note**: The addition of email validation emphasizes the importance of ensuring that the `email` parameter provided during the instantiation of a `User` object, as well as when updating the email, are strings in a valid email format. The ID is generated internally and is not intended to be modified directly.

**Input Example**: 

```
user1 = User("John Doe", "john.doe@example.com")
```
This code snippet demonstrates how to create a new instance of the `User` class with "John Doe" as the name and "john.doe@example.com" as the email address.

**Output Example**:

```
print(user1)
```
Executing the print function on a `User` instance will produce an output similar to: `User [ID: <unique_id>, Name: John Doe, Email: john.doe@example.com]`. Here, `<unique_id>` represents the automatically generated unique identifier for the user.

This updated documentation ensures clarity and completeness, reflecting the current functionalities of the `User` class, including the newly added email validation feature for the update_email method.
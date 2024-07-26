# user.py

## ClassDef User

The function of the class is to represent a user with a unique ID, name, and email address.

**Attributes**:

- `id` (`UUID`): A unique identifier for the user, generated using the uuid library.
- `name` (`str`): The name of the user.
- `email` (`str`): The email address of the user.

**Functions**:

- `__init__`(`name`: `str`, `email`: `str`)
    - Parameters:
        - `name` (`str`): The name of the user.
        - `email` (`str`): The email address of the user.
    - Returns:
        - No explicit return value but initializes a User instance.

- `__str__`() -> `str`
    - Parameters:
        - None
    - Returns:
        - `str`: A string representation of the User instance.

- `update_email`(`new_email`: `str`)
    - Parameters:
        - `new_email` (`str`): The new email address for the user.
    - Returns:
        - No explicit return value but updates the user's email address.

**Code Description**: The `User` class in this file is designed to encapsulate the properties and behaviors associated with a user entity. It leverages the `uuid` library to ensure each user instance has a unique identifier. The class provides a method to update the user's email, demonstrating encapsulation and the ability to modify instance attributes safely.

**Note**: When using the `User` class, ensure that the `name` and `email` parameters provided during instantiation are of type `str`. The `uuid` library is used to generate a unique identifier for each user instance, which means each `User` object will have a distinct `id` attribute.

**Input Example**: 

```
user1 = User("John Doe", "john.doe@example.com")
```
This example demonstrates how to create a new `User` instance with a name and email address.

**Output Example**:

```
print(user1)
```
This will output something similar to:
```
User [ID: 123e4567-e89b-12d3-a456-426614174000, Name: John Doe, Email: john.doe@example.com]
```
This output example shows the string representation of a `User` instance, including its unique ID, name, and email address.
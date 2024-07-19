# User Documentation

## Overview

This documentation provides details on the `User` class, which is designed to represent a user with a unique identifier, name, and email address. The class leverages the `uuid` library to generate a unique identifier (`UUID`) for each user instance, ensuring that each user can be distinctly identified.

## Class Definition: User

The `User` class encapsulates user-related information, including a unique ID, name, and email address. It offers functionality to update a user's email address and to represent the user instance as a string.

### Attributes

- `id` (`UUID`): A unique identifier for the user, automatically generated upon instance creation using the `uuid` library.
- `name` (`str`): The user's name.
- `email` (`str`): The user's email address.

### Methods

#### `__init__(self, name: str, email: str) -> None`

Constructor for initializing a new `User` instance with the specified name and email.

- **Parameters**:
    - `name` (`str`): The name of the user.
    - `email` (`str`): The email address of the user.
- **Returns**: 
    - `None`

#### `__str__(self) -> str`

Provides a string representation of the `User` instance, including the unique ID, name, and email address.

- **Returns**:
    - `str`: A string that represents the `User` instance.

#### `update_email(self, new_email: str) -> None`

Updates the email address of the `User` instance.

- **Parameters**:
    - `new_email` (`str`): The new email address for the user.
- **Returns**:
    - `None`

### Code Description

The `User` class is designed to create user instances with unique identifiers, names, and email addresses. It includes a method for updating the email address of a user and another method for generating a string representation of the user. The class relies on the `uuid` library for generating unique identifiers for each user instance.

### Important Note

When utilizing the `User` class, it is important to ensure that the email address provided is valid. The class does not perform any form of email validation.

### Usage Examples

#### Creating a New User Instance

```python
user1 = User("John Doe", "john.doe@example.com")
```

This code snippet demonstrates how to create a new `User` instance with the name "John Doe" and the email "john.doe@example.com".

#### Output Example

```python
print(user1)
```

Executing the above print statement will output:

```
User [ID: <unique_id>, Name: John Doe, Email: john.doe@example.com]
```

Here, `<unique_id>` is a placeholder for the actual UUID generated for the user instance.
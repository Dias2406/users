# User Documentation

## Overview

This documentation provides details on the `User` class, which is designed to represent a user with a unique identifier, name, and email address. The class leverages the `uuid` library to generate a unique identifier (`UUID`) for each user instance. It includes functionalities to initialize a user, update the user's email, and represent the user instance as a string.

## Class Definition: User

The `User` class encapsulates user-related information and provides methods for managing a user's data.

### Attributes

- `id` (`UUID`): A unique identifier for the user, automatically generated upon instance creation.
- `name` (`str`): The name of the user.
- `email` (`str`): The email address of the user.

### Methods

#### `__init__(self, name: str, email: str) -> None`

Initializes a new instance of the `User` class.

- **Parameters**:
    - `name` (`str`): The name of the user.
    - `email` (`str`): The email address of the user.
- **Returns**: None.

#### `__str__(self) -> str`

Returns a string representation of the `User` instance, including the unique ID, name, and email address.

- **Returns**: `str`.

#### `update_email(self, new_email: str) -> None`

Updates the email address of the user instance.

- **Parameters**:
    - `new_email` (`str`): The new email address for the user.
- **Returns**: None.

### Code Description

The `User` class utilizes the `uuid` library to ensure each user instance is assigned a unique identifier (`UUID`). It provides a constructor for initializing user instances with a name and email, a method for updating the user's email address, and a method for obtaining a string representation of the user instance.

### Note

When using the `update_email` method, it is important to ensure that the new email address provided is valid. This method does not perform any validation on the email address.

### Input Example

```python
user = User("John Doe", "john.doe@example.com")
```

This example demonstrates how to create a new user instance with the name "John Doe" and the email "john.doe@example.com".

### Output Example

```
User [ID: 123e4567-e89b-12d3-a456-426614174000, Name: John Doe, Email: john.doe@example.com]
```

This output example illustrates the string representation of a user instance, showcasing the unique ID, name, and email address of the user.
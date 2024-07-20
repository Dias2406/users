# User Documentation

## Overview

This documentation provides details on the `User` class, which is designed to represent a user with a unique identifier, name, and email address. The class leverages the `uuid` library to generate a unique ID for each user instance, ensuring that every user is distinct.

## Class Definition: User

The `User` class encapsulates user-related information, including a unique ID, name, and email address. It provides functionality to initialize a new user and represent the user as a string.

### Attributes

- `id` (`UUID`): A unique identifier for the user, automatically generated upon instance creation to ensure uniqueness.
- `name` (`str`): The user's name.
- `email` (`str`): The user's email address.

### Methods

#### `__init__(self, name: str, email: str) -> None`

Initializes a new instance of the `User` class.

- **Parameters**:
    - `name` (`str`): The name of the user.
    - `email` (`str`): The email address of the user.
- **Returns**: None.

#### `__str__(self) -> str`

Provides a string representation of the `User` instance, including the ID, name, and email.

- **Returns**: `str` - A formatted string containing the user's ID, name, and email address.

### Code Description

The `User` class utilizes the `uuid.uuid4()` method from the `uuid` library to generate a unique identifier (`UUID`) for each user instance. This ensures that each user has a distinct ID. The class includes methods for initializing a user with a name and email and representing the user as a string.

### Examples

#### Creating a New User

**Input Example**:

```python
user = User("John Doe", "john.doe@example.com")
```

This code snippet demonstrates how to create a new `User` instance with the name "John Doe" and the email "john.doe@example.com".

#### String Representation of a User

**Output Example**:

```
User [ID: 123e4567-e89b-12d3-a456-426614174000, Name: John Doe, Email: john.doe@example.com]
```

This output shows the string representation of a `User` instance, including the unique ID, name, and email address of the user.
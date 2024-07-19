# Data Processor Documentation

## Overview

The `DataProcessor` class is designed to perform operations on data, specifically focusing on processing strings and validating email addresses. It leverages a utility function for email validation, ensuring a modular and reusable code structure.

## Class Definition: DataProcessor

The primary purpose of this class is to offer methods for transforming string data and for the validation of email addresses based on specific criteria.

### Attributes

The `DataProcessor` class does not have any explicitly defined attributes.

### Methods

#### `process_data(self, data) -> List[str]`

Transforms a list of strings to uppercase.

- **Parameters**:
    - `data` (`List[str]`): A list containing strings that need to be processed.
- **Returns**:
    - `List[str]`: A new list where each string from the input list is converted to uppercase.

#### `check_emails(self, emails) -> List[bool]`

Validates a list of email addresses.

- **Parameters**:
    - `emails` (`List[str]`): A list containing email addresses to be validated.
- **Returns**:
    - `List[bool]`: A list of boolean values, each corresponding to the validity of the email addresses in the input list, where `True` indicates a valid email and `False` indicates an invalid one.

### Called Functions

- **`validate_email(email: str) -> bool`**: A function imported from `utils.py` that checks if an email address matches a specific regular expression pattern, returning `True` for a match (valid email) and `False` otherwise.

### Code Description

The `DataProcessor` class encapsulates two key functionalities:
- **String Processing**: Through the `process_data` method, it allows for the conversion of each string in a given list to uppercase, facilitating data normalization or other preprocessing needs.
- **Email Validation**: The `check_emails` method utilizes the `validate_email` function to assess the validity of each email address in a provided list, based on a predefined pattern.

### Important Note

To ensure the expected behavior of the `DataProcessor` methods, it is crucial to provide inputs that adhere to the specified types and formats:
- The `process_data` method expects a list of strings.
- The `check_emails` method requires a list of email addresses in string format.

### Input and Output Examples

#### Input Example

```python
data = ["apple", "banana", "cherry"]
emails = ["test@example.com", "invalid-email"]

# Processing string data
processed_data = DataProcessor().process_data(data)

# Validating email addresses
email_validity = DataProcessor().check_emails(emails)
```

#### Output Example

```python
processed_data = ["APPLE", "BANANA", "CHERRY"]
email_validity = [True, False]
```

The output examples illustrate the functionality of the `DataProcessor` class:
- `processed_data` demonstrates the conversion of each input string to uppercase.
- `email_validity` shows the result of email validation, indicating which emails are valid (`True`) and which are not (`False`).
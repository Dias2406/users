# Data Processor Documentation

## Overview

The `DataProcessor` class is designed to perform operations on data, specifically focusing on processing strings and validating email addresses. It leverages a utility function for email validation, ensuring a modular approach to handling data.

## Class Definition: DataProcessor

The primary purpose of this class is to offer methods that allow for the manipulation of string data and the verification of email addresses based on predefined criteria.

### Attributes

The `DataProcessor` class does not have any explicitly defined attributes.

### Methods

#### `process_data(self, data) -> List[str]`

Converts each string in the provided list to uppercase.

- **Parameters**:
    - `data` (`List[str]`): A list containing strings that need to be processed.
- **Returns**:
    - `List[str]`: A new list where each string from the input list has been converted to uppercase.

#### `check_emails(self, emails) -> List[bool]`

Validates each email address in the provided list.

- **Parameters**:
    - `emails` (`List[str]`): A list containing email addresses to be validated.
- **Returns**:
    - `List[bool]`: A list of boolean values, each corresponding to the validity of the email address at the same index in the input list.

### Called Functions

- **`validate_email(email: str) -> bool`**: A function imported from the `utils` module that checks if the provided email address matches a specific regular expression pattern, indicating its validity.

### Code Description

The `DataProcessor` class encapsulates two key functionalities:
- **String Processing**: Through the `process_data` method, it allows for the transformation of a list of strings, converting each element to uppercase.
- **Email Validation**: Utilizing the `check_emails` method, it employs the `validate_email` function to assess the validity of each email address in a given list, returning a corresponding list of boolean values.

### Important Note

The effectiveness of the `check_emails` method in validating email addresses is contingent upon the regular expression used in the `validate_email` function. It is crucial to ensure that this regular expression is comprehensive and aligns with the criteria for valid email addresses.

### Usage Example

#### Input

```python
data = ["apple", "banana", "cherry"]
emails = ["test@example.com", "invalid-email"]

processor = DataProcessor()
print(processor.process_data(data))
print(processor.check_emails(emails))
```

#### Output

```
['APPLE', 'BANANA', 'CHERRY']
[True, False]
```

This example illustrates the application of the `DataProcessor` class in converting a list of strings to uppercase and validating a list of email addresses, showcasing the utility and functionality of the class methods.
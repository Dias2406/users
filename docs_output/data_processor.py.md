# Data Processor Documentation

## Overview

The `DataProcessor` class is designed to perform operations on data, specifically focusing on processing strings and validating email addresses. It utilizes a utility function for email validation, ensuring that each email address adheres to a specific format.

## Class Definition: DataProcessor

The primary purpose of this class is to offer methods for transforming data into a uniform format and for checking the validity of email addresses based on predefined criteria.

### Attributes

The `DataProcessor` class does not have any explicitly defined attributes.

### Methods

#### `process_data(self, data) -> List[str]`

Transforms a list of strings to uppercase.

- **Parameters**:
    - `data` (`List[str]`): A list containing strings that need to be processed.
- **Returns**:
    - `List[str]`: A new list where each string from the input list has been converted to uppercase.

#### `check_emails(self, emails) -> List[bool]`

Validates a list of email addresses.

- **Parameters**:
    - `emails` (`List[str]`): A list containing email addresses to be validated.
- **Returns**:
    - `List[bool]`: A list of boolean values, each corresponding to the validity of the email addresses in the input list. `True` indicates a valid email, while `False` indicates an invalid one.

### Called Functions

- `validate_email(email: str) -> bool`: This function checks if the provided email address matches a specific pattern that denotes a valid email format. It returns `True` for a valid email and `False` for an invalid one.

### Code Description

The `DataProcessor` class encapsulates two main functionalities:
- The `process_data` method, which processes a list of strings by converting each string into uppercase. This method is useful for standardizing text data.
- The `check_emails` method, which assesses the validity of a list of email addresses. It leverages the `validate_email` function from the `utils` module to determine if each email address conforms to a valid format.

### Important Note

The functionality of the `check_emails` method is dependent on the `validate_email` function, which is part of the `utils` module. It is crucial to ensure that this module is correctly imported and accessible within the project environment.

### Usage Example

```python
data = ["apple", "banana", "cherry"]
emails = ["test@example.com", "invalid-email", "another@test.com"]

processor = DataProcessor()
print(processor.process_data(data))
print(processor.check_emails(emails))
```

### Expected Output

```
['APPLE', 'BANANA', 'CHERRY']
[True, False, True]
```

The provided example demonstrates the usage of the `DataProcessor` class for converting a list of strings to uppercase and for validating a list of email addresses. The output clearly shows the processed data and the results of email validation, indicating which emails are valid and which are not.
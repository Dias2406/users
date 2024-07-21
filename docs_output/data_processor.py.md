# Data Processor Documentation

## Overview

The `DataProcessor` class is designed to perform operations on data, specifically focusing on processing textual data and validating email addresses. It leverages a utility function for email validation, ensuring that email addresses conform to a standard format.

## Class Definition: DataProcessor

The primary purpose of this class is to offer methods for transforming data into a uniform format and for assessing the validity of email addresses based on a predefined pattern.

### Attributes

The `DataProcessor` class does not have any explicitly defined attributes.

### Methods

#### `process_data(self, data) -> List[str]`

Transforms a list of string items to uppercase.

- **Parameters**:
    - `data` (`List[str]`): A list containing string items.
- **Returns**:
    - `List[str]`: A new list where each item from the input list has been converted to uppercase.

#### `check_emails(self, emails) -> List[bool]`

Validates a list of email addresses.

- **Parameters**:
    - `emails` (`List[str]`): A list containing email addresses as strings.
- **Returns**:
    - `List[bool]`: A list of boolean values, each corresponding to the validity of the email address at the same index in the input list.

### Called Functions

- `validate_email(email: str) -> bool`: This function checks if the provided email string matches a specific pattern that represents a valid email address format. It returns `True` if the pattern matches (indicating a valid email), and `False` otherwise.

### Code Description

The `DataProcessor` class encapsulates two primary functionalities: data transformation and email validation. The `process_data` method is utilized for converting strings in a list to their uppercase equivalents, which is particularly useful for normalizing text data. The `check_emails` method employs the `validate_email` function from the `utils` module to ascertain the validity of each email address in a given list, returning a list of boolean values that reflect the validation outcome.

### Important Note

It is crucial to ensure that the list of emails provided to the `check_emails` method comprises properly formatted strings to prevent inaccurate validation results.

### Usage Example

```python
data_processor = DataProcessor()
data = ["apple", "banana", "cherry"]
emails = ["test@example.com", "invalid_email", "another_test@example.com"]

print(data_processor.process_data(data))
print(data_processor.check_emails(emails))
```

### Expected Output

```
['APPLE', 'BANANA', 'CHERRY']
[True, False, True]
```

The provided example illustrates the application of the `DataProcessor` class for converting a list of strings to uppercase and for validating a list of email addresses. The output showcases the outcomes of both operations: the `process_data` method returns all items in uppercase, while the `check_emails` method yields a list of boolean values indicating the validity of each email address.
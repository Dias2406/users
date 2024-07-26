# data_processor.py

## ClassDef DataProcessor

The function of the class is to provide methods for processing data and validating email addresses.

**Attributes**:

This class does not have explicitly defined attributes.

**Functions**:

- `process_data(self, data)` -> `List[str]`
    - Parameters:
        - `data` (`List[str]`): A list of data items (strings).
    - Returns:
        - `List[str]`: A new list with each item from the input list converted to uppercase.

- `check_emails(self, emails)` -> `List[bool]`
    - Parameters:
        - `emails` (`List[str]`): A list of email addresses.
    - Returns:
        - `List[bool]`: A list of boolean values indicating the validity of each email address.

**Called_functions**:

- `validate_email(email: str) -> bool`: Checks if the given email address matches the pattern of a valid email. Returns `True` if the email is valid, otherwise `False`.

**Code Description**: The `DataProcessor` class contains two methods: `process_data` for converting data items to uppercase, and `check_emails` for validating email addresses using the `validate_email` function from the `utils` module. The `validate_email` function uses a regular expression to determine the validity of an email address.

**Note**: The `check_emails` method relies on the `validate_email` function from the `utils` module. Ensure that the `utils` module is correctly imported and the `validate_email` function is available.

**Input Example**: 

```
data = ["apple", "banana", "cherry"]
emails = ["user@example.com", "invalid-email", "anotheruser@example.org"]

processor = DataProcessor()
print(processor.process_data(data))
print(processor.check_emails(emails))
```

**Output Example**:

```
['APPLE', 'BANANA', 'CHERRY']
[True, False, True]
```

This example demonstrates how to use the `DataProcessor` class to convert a list of strings to uppercase and validate a list of email addresses. The output shows the results of both operations.
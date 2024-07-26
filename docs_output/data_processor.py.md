# data_processor.py

## ClassDef DataProcessor

The function of the class is to provide methods for processing data and validating email addresses.

**Attributes**:

This class does not explicitly define any attributes.

**Functions**:

- `process_data`(self, `data`: `list`) -> `list`
    - Parameters:
        - `data` (`list`): A list of data items to be processed.
    - Returns:
        - `list`: A new list with each item from the input list converted to uppercase.

- `check_emails`(self, `emails`: `list`) -> `list`
    - Parameters:
        - `emails` (`list`): A list of email addresses to be validated.
    - Returns:
        - `list`: A list of boolean values indicating the validity of each email address.

**Called_functions**:

- `validate_email`(`email`: `str`) -> `bool`: Validates an email address against a regular expression pattern and returns `True` if the email is valid, otherwise `False`.

**Code Description**: The `DataProcessor` class contains two methods: `process_data` for converting data items in a list to uppercase, and `check_emails` for validating a list of email addresses using the `validate_email` function from `utils.py`. The `validate_email` function uses a regular expression to determine the validity of each email address.

**Note**: It is important to ensure that the data passed to `process_data` is a list of strings to avoid type errors. Similarly, for `check_emails`, ensure that a list of valid email address strings is passed for accurate validation.

**Input Example**: 

```
data = ["apple", "banana", "cherry"]
emails = ["test@example.com", "invalid-email"]

processor = DataProcessor()
print(processor.process_data(data))
print(processor.check_emails(emails))
```

**Output Example**:

```
['APPLE', 'BANANA', 'CHERRY']
[True, False]
```

This example demonstrates how to use the `DataProcessor` class to convert a list of strings to uppercase and validate a list of email addresses, showing the expected output for each method.
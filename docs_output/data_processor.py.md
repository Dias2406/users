# Data Processor Documentation

## Overview

The `DataProcessor` class is designed to perform operations on data, specifically focusing on processing generic data items and validating email addresses. It leverages a utility function for email validation, ensuring that each email address adheres to a predefined format. This document outlines the functionalities provided by the `DataProcessor` class, including method descriptions, parameters, return values, and examples of usage.

## Class Definition: DataProcessor

The `DataProcessor` class encapsulates methods for data manipulation and email validation without maintaining any internal state.

### Methods

#### `process_data`

Converts each item in a given list to uppercase.

- **Parameters**:
    - `data` (`list`): A list of strings to be processed.
- **Returns**:
    - `list`: A new list containing the uppercase versions of the input list's items.

#### `check_emails`

Validates a list of email addresses using a predefined pattern.

- **Parameters**:
    - `emails` (`list`): A list of email addresses to be validated.
- **Returns**:
    - `list`: A list of boolean values, each corresponding to the validity of the email address at the same index in the input list.

### Called Functions

- **`validate_email(email: string) -> bool`**: 
    - Utilized within the `check_emails` method, this function checks if the provided email address matches a specific pattern that defines a valid email format. It returns `True` if the pattern matches (indicating validity), and `False` otherwise.

### Code Description

The `DataProcessor` class offers two primary functionalities:

1. **Data Processing**: Through the `process_data` method, it allows for the transformation of textual data, specifically by converting each item in a provided list to uppercase. This can be useful for standardizing data for further processing or analysis.

2. **Email Validation**: The `check_emails` method leverages the `validate_email` function from an external utility module to assess the validity of each email address in a provided list. This method is essential for filtering out invalid email addresses based on a specific validation pattern.

### Note

The accuracy of the `check_emails` method's output heavily relies on the `validate_email` function's ability to correctly identify valid and invalid email formats. It is important to ensure that the email addresses passed to this method are formatted correctly for validation purposes.

### Input and Output Examples

- **Input Example**:

    ```python
    data = ["apple", "banana", "cherry"]
    emails = ["user@example.com", "invalid-email", "another@valid.com"]
    ```

- **Output Example**:

    ```python
    Processed data: ["APPLE", "BANANA", "CHERRY"]
    Email validation: [True, False, True]
    ```

This documentation aims to provide a clear and comprehensive guide to the `DataProcessor` class, detailing its methods, functionalities, and practical applications in data processing and email validation tasks.
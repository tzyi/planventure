# Password Utilities Usage Examples

## Overview

This project includes secure password hashing and verification utilities using bcrypt with automatic salt generation.

## Files Created

- `utils/password_utils.py` - Main password utility functions
- `models/user.py` - Updated User model with password methods
- `test_password_utils_simple.py` - Test script

## Usage Examples

### 1. Direct Function Usage

```python
from utils.password_utils import hash_password, verify_password

# Hash a password
password = "my_secure_password"
hashed = hash_password(password)
print(f"Hashed: {hashed}")

# Verify a password
is_valid = verify_password(password, hashed)
print(f"Valid: {is_valid}")  # True

is_invalid = verify_password("wrong_password", hashed)
print(f"Invalid: {is_invalid}")  # False
```

### 2. User Model Usage

```python
from models.user import User

# Create a new user
user = User()
user.email = "user@example.com"

# Set password (automatically hashed)
user.set_password("secure_password_123")

# Check password
if user.check_password("secure_password_123"):
    print("Password is correct!")
else:
    print("Invalid password!")

# Get user data without sensitive information
user_data = user.to_dict()
print(user_data)  # No password_hash included
```

### 3. Class-based Usage

```python
from utils.password_utils import PasswordUtils

utils = PasswordUtils()

# Hash password
hashed = utils.hash_password("my_password")

# Verify password
is_valid = utils.verify_password("my_password", hashed)

# Generate custom salt
salt = utils.generate_salt()

# Hash with specific salt
custom_hash = utils.hash_password_with_salt("my_password", salt)
```

## Security Features

- **bcrypt hashing**: Industry-standard password hashing algorithm
- **Automatic salt generation**: Each password gets a unique salt
- **Configurable work factor**: Default bcrypt rounds for security vs performance
- **Input validation**: Proper error handling for invalid inputs
- **No plain text storage**: Passwords are never stored in plain text

## API Reference

### Functions

#### `hash_password(password: str) -> str`
Hash a password with automatic salt generation.

#### `verify_password(password: str, password_hash: str) -> bool`
Verify a password against its hash.

#### `generate_salt() -> str`
Generate a new salt for password hashing.

#### `hash_password_with_salt(password: str, salt: str) -> str`
Hash a password with a specific salt.

### User Model Methods

#### `user.set_password(password: str) -> None`
Set the user's password (automatically hashed).

#### `user.check_password(password: str) -> bool`
Check if provided password matches user's password.

#### `user.to_dict() -> dict`
Get user data excluding sensitive information.

## Testing

Run the test script to verify functionality:

```bash
python3 test_password_utils_simple.py
```

## Error Handling

The utilities include proper error handling:

- Empty or None passwords raise `ValueError`
- Invalid hash formats return `False` for verification
- Malformed salts are handled gracefully

## Dependencies

Make sure bcrypt is installed:

```bash
pip install bcrypt==4.0.1
```

This is already included in `requirements.txt`.

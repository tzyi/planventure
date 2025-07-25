"""
Password utility functions for secure password hashing and verification.
Uses bcrypt for secure password hashing with salt.
"""

import bcrypt


class PasswordUtils:
    """
    Utility class for password hashing and verification using bcrypt.
    """
    
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a password using bcrypt with a generated salt.
        
        Args:
            password (str): The plain text password to hash
            
        Returns:
            str: The hashed password as a string
            
        Raises:
            ValueError: If password is empty or None
        """
        if not password:
            raise ValueError("Password cannot be empty or None")
        
        # Generate salt and hash password
        # bcrypt.gensalt() automatically generates a random salt
        salt = bcrypt.gensalt()
        
        # Hash the password with the salt
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        # Return as string (bcrypt returns bytes)
        return hashed.decode('utf-8')
    
    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        """
        Verify a password against its hash.
        
        Args:
            password (str): The plain text password to verify
            password_hash (str): The stored password hash
            
        Returns:
            bool: True if password matches hash, False otherwise
            
        Raises:
            ValueError: If password or password_hash is empty or None
        """
        if not password:
            raise ValueError("Password cannot be empty or None")
        
        if not password_hash:
            raise ValueError("Password hash cannot be empty or None")
        
        try:
            # bcrypt.checkpw handles the salt extraction automatically
            return bcrypt.checkpw(
                password.encode('utf-8'), 
                password_hash.encode('utf-8')
            )
        except (ValueError, TypeError):
            # Invalid hash format or other bcrypt errors
            return False
    
    @staticmethod
    def generate_salt() -> str:
        """
        Generate a new salt for password hashing.
        
        Returns:
            str: A new salt as a string
        """
        salt = bcrypt.gensalt()
        return salt.decode('utf-8')
    
    @staticmethod
    def hash_password_with_salt(password: str, salt: str) -> str:
        """
        Hash a password with a specific salt.
        
        Args:
            password (str): The plain text password to hash
            salt (str): The salt to use for hashing
            
        Returns:
            str: The hashed password as a string
            
        Raises:
            ValueError: If password or salt is empty or None
        """
        if not password:
            raise ValueError("Password cannot be empty or None")
        
        if not salt:
            raise ValueError("Salt cannot be empty or None")
        
        # Hash the password with the provided salt
        hashed = bcrypt.hashpw(
            password.encode('utf-8'), 
            salt.encode('utf-8')
        )
        
        return hashed.decode('utf-8')


# Convenience functions for easier import and usage
def hash_password(password: str) -> str:
    """
    Convenience function to hash a password.
    
    Args:
        password (str): The plain text password to hash
        
    Returns:
        str: The hashed password
    """
    return PasswordUtils.hash_password(password)


def verify_password(password: str, password_hash: str) -> bool:
    """
    Convenience function to verify a password.
    
    Args:
        password (str): The plain text password
        password_hash (str): The stored password hash
        
    Returns:
        bool: True if password matches hash, False otherwise
    """
    return PasswordUtils.verify_password(password, password_hash)


def generate_salt() -> str:
    """
    Convenience function to generate a new salt.
    
    Returns:
        str: A new salt
    """
    return PasswordUtils.generate_salt()


def hash_password_with_salt(password: str, salt: str) -> str:
    """
    Convenience function to hash a password with a specific salt.
    
    Args:
        password (str): The plain text password
        salt (str): The salt to use
        
    Returns:
        str: The hashed password
    """
    return PasswordUtils.hash_password_with_salt(password, salt)

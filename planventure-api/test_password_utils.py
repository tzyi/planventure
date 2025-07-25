#!/usr/bin/env python3
"""
Test script for password utilities.
Run this script to verify that password hashing and verification work correctly.
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.password_utils import (
    hash_password, 
    verify_password, 
    generate_salt, 
    hash_password_with_salt,
    PasswordUtils
)


def test_password_utilities():
    """Test all password utility functions."""
    print("🔐 Testing Password Utilities...")
    print("-" * 50)
    
    # Test 1: Basic password hashing and verification
    print("Test 1: Basic password hashing and verification")
    password = "test_password_123"
    hashed = hash_password(password)
    
    print(f"Original password: {password}")
    print(f"Hashed password: {hashed}")
    print(f"Hash length: {len(hashed)} characters")
    
    # Verify correct password
    is_valid = verify_password(password, hashed)
    print(f"✅ Correct password verification: {is_valid}")
    assert is_valid, "Password verification should succeed for correct password"
    
    # Verify incorrect password
    is_invalid = verify_password("wrong_password", hashed)
    print(f"❌ Incorrect password verification: {is_invalid}")
    assert not is_invalid, "Password verification should fail for incorrect password"
    
    print()
    
    # Test 2: Multiple hashes of same password should be different
    print("Test 2: Multiple hashes of same password")
    hash1 = hash_password(password)
    hash2 = hash_password(password)
    
    print(f"Hash 1: {hash1}")
    print(f"Hash 2: {hash2}")
    print(f"✅ Hashes are different: {hash1 != hash2}")
    assert hash1 != hash2, "Multiple hashes of same password should be different (due to salt)"
    
    # Both should verify correctly
    assert verify_password(password, hash1), "First hash should verify correctly"
    assert verify_password(password, hash2), "Second hash should verify correctly"
    
    print()
    
    # Test 3: Salt generation and custom salt usage
    print("Test 3: Salt generation and custom salt usage")
    salt = generate_salt()
    print(f"Generated salt: {salt}")
    print(f"Salt length: {len(salt)} characters")
    
    # Hash with custom salt
    custom_hash = hash_password_with_salt(password, salt)
    print(f"Hash with custom salt: {custom_hash}")
    
    # Same password with same salt should produce same hash
    custom_hash2 = hash_password_with_salt(password, salt)
    print(f"✅ Same salt produces same hash: {custom_hash == custom_hash2}")
    assert custom_hash == custom_hash2, "Same password with same salt should produce same hash"
    
    print()
    
    # Test 4: Error handling
    print("Test 4: Error handling")
    
    try:
        hash_password("")
        assert False, "Should raise ValueError for empty password"
    except ValueError as e:
        print(f"✅ Empty password error: {e}")
    
    try:
        hash_password(None)
        assert False, "Should raise ValueError for None password"
    except ValueError as e:
        print(f"✅ None password error: {e}")
    
    try:
        verify_password("password", "")
        assert False, "Should raise ValueError for empty hash"
    except ValueError as e:
        print(f"✅ Empty hash error: {e}")
    
    # Test invalid hash format
    invalid_result = verify_password("password", "invalid_hash_format")
    print(f"✅ Invalid hash format returns False: {not invalid_result}")
    assert not invalid_result, "Invalid hash format should return False"
    
    print()
    
    # Test 5: Class-based usage
    print("Test 5: Class-based usage")
    utils = PasswordUtils()
    class_hash = utils.hash_password(password)
    class_verify = utils.verify_password(password, class_hash)
    
    print(f"✅ Class-based hashing works: {class_verify}")
    assert class_verify, "Class-based password utilities should work"
    
    print()
    print("🎉 All tests passed! Password utilities are working correctly.")


def test_user_model():
    """Test the User model password methods."""
    print("\n👤 Testing User Model Password Methods...")
    print("-" * 50)
    
    # Import here to avoid circular imports during testing
    from models.user import User
    
    # Create a user instance (not saving to database)
    user = User()
    user.email = "test@example.com"
    
    # Test setting password
    password = "secure_password_123"
    user.set_password(password)
    
    print(f"Original password: {password}")
    print(f"Stored hash: {user.password_hash}")
    print(f"Hash length: {len(user.password_hash)} characters")
    
    # Test password verification
    correct_check = user.check_password(password)
    print(f"✅ Correct password check: {correct_check}")
    assert correct_check, "User should verify correct password"
    
    incorrect_check = user.check_password("wrong_password")
    print(f"❌ Incorrect password check: {incorrect_check}")
    assert not incorrect_check, "User should reject incorrect password"
    
    # Test to_dict method
    user_dict = user.to_dict()
    print(f"✅ User dict (no password): {user_dict}")
    assert 'password_hash' not in user_dict, "to_dict should not include password_hash"
    assert 'email' in user_dict, "to_dict should include email"
    
    # Test __repr__ method
    user.id = 1
    repr_str = repr(user)
    print(f"✅ User representation: {repr_str}")
    assert "test@example.com" in repr_str, "__repr__ should include email"
    
    print("\n🎉 User model tests passed!")


if __name__ == "__main__":
    print("Starting Password Utilities Tests...\n")
    
    try:
        test_password_utilities()
        test_user_model()
        
        print("\n" + "="*60)
        print("🚀 ALL TESTS COMPLETED SUCCESSFULLY! 🚀")
        print("="*60)
        print("\nPassword utilities are ready for use in your application!")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

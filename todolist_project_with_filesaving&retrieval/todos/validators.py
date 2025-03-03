from django.core.exceptions import ValidationError
import re


# Custom password validators
class CustomPasswordValidator:
    """
    This validator checks for the following rules:
    1. Password length should be at least 8 characters.
    2. Password should contain at least one uppercase letter.
    3. Password should contain at least one special character (like @, #, $, etc.).
    """
    
    def __init__(self):
        self.min_password_length = 8
        
    def validate(self, password, user=None):
        # Check password length
        if len(password) < self.min_password_length:
            raise ValidationError("Password must be at least 8 characters long.")
        
        # Check for at least one uppercase letter
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one upper case letter.")
        
        # Check for at least one special character
        if not re.search(r'[\W_]', password):
            raise ValidationError("Password must contain atleast one special character (like @, #, $, etc.)")
        
    def get_help_text(self):
            return "Your password must be at least 8 characters long, contain at least one uppercase letter, and include one special character (like @, #, $, etc.)."
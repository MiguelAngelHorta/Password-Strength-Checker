import re

def check_password_strength(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."
    
    # Check if the password contains both uppercase and lowercase letters
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "Password should contain both uppercase and lowercase letters."
    
    # Check if the password contains at least one digit
    if not re.search("[0-9]", password):
        return "Password should contain at least one digit."
    
    # Check if the password contains at least one special character
    if not re.search("[!@#$%^&*()-_=+]", password):
        return "Password should contain at least one special character (!@#$%^&*()-_=+)."
    
    # Password passed all checks
    return "Password is strong."

def main():
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()

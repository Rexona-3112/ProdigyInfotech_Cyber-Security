import re

def check_password_strength(password, forbidden_words):
    """
    Check the strength of the given password and ensure it doesn't contain forbidden words.
    
    Args:
        password (str): The password to check.
        forbidden_words (list): List of forbidden words to check against.
    
    Returns:
        str: Feedback about the password strength.
    """
    # Check if password contains any forbidden words
    for word in forbidden_words:
        if word.lower() in password.lower():
            return f"❌ Password includes forbidden words like '{word}'. Avoid using personal information in your password! 🚫"

    # Criteria
    length_criteria = len(password) >= 12
    upper_criteria = any(char.isupper() for char in password)
    lower_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Count the number of met criteria
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
    
    # Strength and Feedback
    if criteria_met == 5:
        return "🌟 Excellent Password! It's highly secure. Keep it up! 🔒"
    elif criteria_met == 4:
        return "😊 Good Password! Try adding more special characters or numbers for extra security. 💡"
    elif criteria_met == 3:
        return "🙂 Decent Password! Consider increasing its length or mixing case for better strength. 🛠️"
    elif criteria_met == 2:
        return "😐 Weak Password. Add uppercase, numbers, and special characters to make it stronger. ⚠️"
    else:
        return "😟 Very Weak Password. Make it longer and include a mix of letters, numbers, and symbols. ❌"

def main():
    print("🔑 Password Complexity Checker 🔍")
    username = input("Enter your First Name: ").strip()
    surname = input("Enter your Last Name: ").strip()
    
    forbidden_words = [username, surname]  # Use the correct variable names
    password = input("Enter your password: ").strip()
    
    feedback = check_password_strength(password, forbidden_words)
    print("\n" + feedback)

if __name__ == "__main__":
    main()

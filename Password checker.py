import re

def check_password_strength(password):
    # Define criteria
    length_criteria = 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_character_criteria = bool(re.search(r'[@_!#$%^&*()<>?/\|}{~:]', password))

    # Calculate score
    score = 0
    if len(password) >= length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_character_criteria:
        score += 1

    # Assess strength
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

def main():
    while True:
        password = input("Enter your password: ")

        # Check password strength
        strength = check_password_strength(password)

        print(f"Password strength: {strength}")

        choice = input("Do you want to check another password? (yes/no): ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()

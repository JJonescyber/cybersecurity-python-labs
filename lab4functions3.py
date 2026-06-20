def check_strength(password):
    if len(password) < 6:
        return "Weak password"
    elif password.isalpha():
        return "Moderate password"
    elif any(char.isdigit() for char in password) and any(not char.isalnum() for char in password):
        return "Strong password"
    else:
        return "Moderate password"

user_pass = input("Enter a password to test: ")
print(check_strength(user_pass))

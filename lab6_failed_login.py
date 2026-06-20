# Failed login counter challenge

correct_password = "python123"
max_attempts = 5

for attempt in range(max_attempts):
    user_pass = input("Enter your password: ")
    
    if user_pass == correct_password:
        print("Welcome!")
        break
    else:
        print("Login failed. Attempt", attempt + 1, "of", max_attempts)

if user_pass != correct_password:
    print("System locked. Please contact administrator.")

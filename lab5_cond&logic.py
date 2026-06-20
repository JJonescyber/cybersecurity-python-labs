# Login simulation using a while loop
password = "secure123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")
    
    if user_input == password:
        print("Access granted.")
        break
    else:
        print("Incorrect password.")
        attempts += 1

if attempts == max_attempts:
    print("Account locked! Too many failed attempts.")

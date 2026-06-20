username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "admin1234":
    print("Welcome, admin Access granted.")
elif username == "user" and password == "passweord123": 
    print("Welcome to the system")   
else:
    print("Invalid credentials Access denied.")
# Simulated log entries
logs = [
    "Login successful: user=alice",
    "Login failed: user=bob",
    "Password change: user=charlie",
    "Login failed: user=dave"
]

# Function to count failed logins
def count_failed_logins(log_entries):
    count = 0
    for entry in log_entries:
        if "failed" in entry:
            count += 1
    return count

failed_attempts = count_failed_logins(logs)
print("Total failed login attempts:", failed_attempts)

import string
import random

# Function to generate a random strong password
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# List of sample passwords to check
passwords = ["12345", "secure!", "Pass2025!", "abc"]

# Function to evaluate password strength
def check_strength(password):
    if len(password) < 6:
        return "Weak"
    elif password.isalpha():
        return "Moderate"
    else:
        return "Strong"

# Automate checking passwords
for pwd in passwords:
    strength = check_strength(pwd)
    print(f"Password: {pwd} - Strength: {strength}")
    if strength == "Weak":
        print("Suggested strong password:", generate_password())

        import random
import time

# List of simulated IPs
ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

# Function to simulate checking IP status
def check_ip_status(ip):
    return random.choice(["Active", "Inactive"])

# Automate network monitoring
for ip in ips:
    status = check_ip_status(ip)
    print(f"IP: {ip} - Status: {status}")
    time.sleep(1)  # Wait 1 second to simulate scanning delay

import string
import random

# Sample user data
users = [
    {"username": "alice", "password": "123"},
    {"username": "bob", "password": "securePass"},
    {"username": "charlie", "password": "pass123!"}
]

# Password strength function
def check_strength(password):
    if len(password) < 6:
        return "Weak"
    elif password.isalpha():
        return "Moderate"
    else:
        return "Strong"

# Open log file
with open("security_report.txt", "w") as report:
    for user in users:
        strength = check_strength(user["password"])
        if strength == "Weak":
            report.write(f"Weak password detected for {user['username']}\n")
        print(f"{user['username']} - Password Strength: {strength}")

print("\nSecurity report saved to security_report.txt")
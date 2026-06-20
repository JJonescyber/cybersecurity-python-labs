total = 0
for i in range(1, 11):
    total += i

print("Sum of numbers from 1 to 10:", total)

def sum_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print("Sum of numbers from 1 to 20:", sum_numbers(20))

users = ["alice", "bob", "charlie", "dave"]

def find_user(username):
    for user in users:
        if user == username:
            return "User found: " + user
    return "User not found"

print(find_user("bob"))
print(find_user("eve"))

# Example: Check multiple passwords for strength
passwords = ["pass123", "Strong!1", "abc", "Cyber2025!"]

def check_strength(password):
    if len(password) < 6:
        return "Weak"
    elif password.isalpha():
        return "Moderate"
    else:
        return "Strong"

for pwd in passwords:
    print(pwd, "-", check_strength(pwd))

    import random

ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

def scan_ip(ip):
    # Randomly simulate active/inactive
    status = random.choice(["active", "inactive"])
    return status

for ip in ips:
    print("IP:", ip, "- Status:", scan_ip(ip))
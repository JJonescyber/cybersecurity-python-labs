# Open a file in write mode
file = open("example_log.txt", "w")

# Write data to the file
file.write("2025-10-21 10:00 - Login attempt successful\n")
file.write("2025-10-21 10:05 - Login attempt failed\n")
file.write("2025-10-21 10:15 - Password change\n")

# Close the file
file.close()
# Open the file in read mode
file = open("example_log.txt", "r")

# Read the content
content = file.read()
print(content)

# Close the file
file.close()
# Open file and read line by line
file = open("example_log.txt", "r")

for line in file:
    print("Log entry:", line.strip())  # strip() removes extra newlines

file.close()
# Open the file in append mode
file = open("example_log.txt", "a")

file.write("2025-10-21 10:30 - User logout\n")
file.write("2025-10-21 10:35 - Login attempt successful\n")

file.close()

# Initialize counters
success_count = 0
fail_count = 0

# Open and read the file
with open("example_log.txt", "r") as file:
    for line in file:
        if "successful" in line:
            success_count += 1
        elif "failed" in line:
            fail_count += 1

# Print results
print("Number of successful logins:", success_count)
print("Number of failed logins:", fail_count)

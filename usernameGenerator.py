print("Welcome!")
firstName = input("Enter your first name...")
lastName = input("Enter your last name...")
firstName = firstName[0:1]
print(firstName)
username = (firstName + lastName)
print(username)
answer = input("This is your username. Is this okay? (y or n)")
if answer == "y":
    file = open("logins.txt", "a")
    with open("logins.txt") as f:
            file.write("\n")
            file.write(username)
            print("Success!")
answer = input("Would you like to create a password? (y or n)")
if answer == "y":
    print("For the best security, make sure you password contains upper and lowercase"
          "letters, numbers, and special characters.")
    password = input("Enter your password here...")
    print(password)
    answer = input("This is your password. Is this okay? (y or n)")
    if answer == "y":
        file = open("logins.txt", "a")
    with open("logins.txt") as f:
        file.write("    ")
        file.write(password)
else: print("Goodbye.")
# :)
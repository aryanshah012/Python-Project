def validate_password(password, username, last_three_passwords):
    if len(password) < 10:
        return False

    if (sum(1 for c in password if c.isupper()) < 2 or
        sum(1 for c in password if c.islower()) < 2 or
        sum(1 for c in password if c.isdigit()) < 2 or
        sum(1 for c in password if not c.isalnum()) < 2):
        return False
    
    if any(username[i:i+3] in password for i in range(len(username) - 2)):
        return False
    
    if any(password.count(c*4) > 0 for c in set(password)):
        return False
    
    if password in last_three_passwords:
        return False
    
    return True

def main():
    username = input("Enter username: ")
    last_three_passwords = []

    while True:
        password = input("Enter new password: ")
        if validate_password(password, username, last_three_passwords):
            print("Password successfully set.")
            break
        else:
            print("Invalid password. Please try again.")

if __name__ == "__main__":
    main()

# adduser.py
from password_utils import read_passwords, write_passwords, encrypt_password
import getpass

def add_user():
    """
    This function adds a new user by prompting for a new username, real name, and password. 
    It checks if the username already exists and if not, it encrypts the password and 
    adds the new user to the list of user credentials. It then writes the updated list 
    of user credentials to the file. This function does not take any parameters and does 
    not return anything.
    """

    usernames = [user[0] for user in read_passwords()]
    
    new_username = input("Enter new username: ").lower()
    
    if new_username in usernames:
        print("Cannot add. Most likely username already exists.")
        return

    real_name = input("Enter real name: ")
    password = getpass.getpass("Password: ")

    encrypted_password = encrypt_password(password)
    
    passwords = read_passwords()
    passwords.append((new_username, real_name, encrypted_password))
    
    write_passwords(passwords)
    print("User Created.")

if __name__ == "__main__":
    add_user()

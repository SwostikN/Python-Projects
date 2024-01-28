# deluser.py
from password_utils import read_passwords, write_passwords

def delete_user():
    """
    Delete a user from the list of usernames and passwords.
    This function prompts the user for a username to delete. It then reads the 
    passwords, removes the user from the list, and writes the updated list of 
    passwords. If the user is not found, it prints "User not found." If the user 
    is successfully deleted, it prints "User Deleted."
    """

    usernames = [user[0] for user in read_passwords()]
    
    username_to_delete = input("Enter username: ").lower()
    
    passwords = read_passwords()
    updated_passwords = [user for user in passwords if user[0] != username_to_delete]

    if len(passwords) == len(updated_passwords):
        print("User not found.")
        return

    write_passwords(updated_passwords)
    print("User Deleted.")

if __name__ == "__main__":
    delete_user()

# passwd.py

from password_utils import read_passwords, write_passwords, encrypt_password
import getpass

def change_password(username):
    """
    Change the password for a user.
    Prompts the user for their current password, new password, and confirmation of the new password.
    If the new password does not match the confirmation password, prints "Passwords do not match" and returns.
    If the current password is not valid, prints "Invalid current password".
    Otherwise, updates the password and prints "Password changed".
    """
    usernames = [user[0] for user in read_passwords()]

    if username not in usernames:
        print("User not found.")
        return

    current_password = getpass.getpass("Current Password: ")
    new_password = getpass.getpass("New Password: ")
    confirm_password = getpass.getpass("Confirm: ")

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    encrypted_current_password = encrypt_password(current_password)

    passwords = read_passwords()
    for i, user in enumerate(passwords):
        if user[0] == username and user[2] == encrypted_current_password:
            passwords[i] = (user[0], user[1], encrypt_password(new_password))
            write_passwords(passwords)
            print("Password changed.")
            return

    print("Invalid current password.")

if __name__ == "__main__":
    # Example usage when running passwd.py directly
    change_password("example_user")

POSITIVE_ANSWER = " y"


def main():
    email_to_name = {}
    email = input("Email: ")
    add_pairs_to_dictionary(email, email_to_name)
    print_email_dictionary(email_to_name)


def add_pairs_to_dictionary(email, email_to_name):
    """Add email and its owner's name to email_to_name dictionary"""
    while email != "":
        name = (email.replace((email[email.find("@"):]), "")).title()
        if "." in name:
            name = name.replace('.', " ").title()
        choice = input(f"Is your name {name.title()} (Y/n) ").lower()
        if choice not in POSITIVE_ANSWER:
            name = input("Name: ")
        email_to_name[name] = email
        email = input("Email: ")


def print_email_dictionary(email_to_name):
    """Print all names and emails from dictionary"""
    for name in email_to_name:
        print(f"{name} ({email_to_name[name]})")


main()
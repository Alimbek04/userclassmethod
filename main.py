from datetime import datetime
from user import User
from user_service import UserService
from user_util import UserUtil


def main():
    # Create a new user
    user_id = UserUtil.generate_user_id()
    name = "Adil"
    surname = "Toktosunov"
    birthday = datetime(2004, 6, 16)

    user = User(user_id, name, surname, birthday)
    user.email = UserUtil.generate_email(name, surname, "example.com")
    user.password = UserUtil.generate_password()

    # Add user to UserService
    UserService.add_user(user)

    # Display user details
    print(user.get_details())
    print(f"User  Age: {user.get_age()}")

    # Find user
    found_user = UserService.find_user(user_id)
    if found_user:
        print("User  found:", found_user.get_details())

    # Total number of users
    print("Total number of users:", UserService.get_number())

    # Update user
    updated_user = User(1, "Adil", "T", datetime(2004, 6, 16))
    updated_user.email = UserUtil.generate_email("Adil", "T", "example.com")
    UserService.update_user(user_id, updated_user)

    # Display updated user details
    updated_found_user = UserService.find_user(user_id)
    if updated_found_user:
        print("Updated user details:", updated_found_user.get_details())

    # Delete user
    UserService.delete_user(user_id)
    print("User  deleted. Total number of users:", UserService.get_number())


if __name__ == '__main__':
    main()
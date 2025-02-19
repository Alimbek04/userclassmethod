from user import User

class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            cls.users[user_id].name = user_update.name
            cls.users[user_id].surname = user_update.surname
            cls.users[user_id].email = user_update.email
            cls.users[user_id].password = user_update.password
            cls.users[user_id].birthday = user_update.birthday

    @classmethod
    def get_number(cls):
        return len(cls.users)
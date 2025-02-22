import random
import re
from datetime import datetime

class UserUtil:
    @staticmethod
    def generate_user_id():
        year = datetime.now().year % 100  # Get last two digits of the year
        random_digits = random.randint(100000, 999999)  # Generate 6 random digits
        return f"{year:02d}{random_digits}"

    @staticmethod
    def generate_password():
        while True:
            password = ''.join(random.choices('adilbeK1!@#$%^&*()', k=12))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
        return (len(password) >= 8 and
                re.search(r'[A-Z]', password) and
                re.search(r'[a-z]', password) and
                re.search(r'[0-9]', password) and
                re.search(r'[!@#$%^&*()]', password))

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
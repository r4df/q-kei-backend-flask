from flask_login import UserMixin

# User model
class User(UserMixin):
    def __init__(self, id):
        self.id = id
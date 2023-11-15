from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, user_name, first_name, last_name, email, password):
        self.id = id
        self.user_name = user_name
        self.full_name = first_name
        self.full_name = last_name
        self.email = email
        self.password = password

    @property
    def is_authenticated(self):
        return True

    def is_authenticated(self, password):
        return self.password == password

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.user_name}, {self.first_name}, {self.last_name}, {self.email}, {self.password})"

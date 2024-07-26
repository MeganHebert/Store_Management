class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def user_dict(self):
        return {
            self.username: self.password,
        }


class UserList:
    def __init__(self):
        self.user_list = []


class CurrentUser:
    def __init__(self):
        self.stored_user = None

    def store_user(self, string):
        self.stored_user = string

    def get_current_user(self):
        return self.stored_user
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, password = None, email = None):
        self.__id = id
        self.__email = email
        self.__password = password
        self.__current_room = None


    def get_id(self):
        return self.__id

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
    
    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = None

    def get_friends_amount(self):
        return len(self.__friends)


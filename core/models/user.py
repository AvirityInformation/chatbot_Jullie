import models


class User:
    """
    This is a simple model for user.
    To fetch user data from db, use User class in models.py
    """

    def __init__(self, user_id):
        self.__id = user_id

        user_data = models.User.find_by_id(user_id)
        self.__sender_id = user_data[0]
        self.__first_name = user_data[1]
        self.__status = user_data[2]

    def update_status(self, status):
        """
        status must be enum. fix it.
        :param status:
        :return:
        """
        models.User.update_status(status, self.id)
        self.status = status

    @property
    def id(self):
        return self.__id

    @property
    def sender_id(self):
        return self.__sender_id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

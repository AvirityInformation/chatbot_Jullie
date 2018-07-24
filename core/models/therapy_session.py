from datetime import datetime, timedelta
import models
from common.constant.session_status import SessionStatus


class TherapySession:
    """
    Therapy session means a certain period of time where bot gives psychotherapy.
    As real CCT method, after finishing session, users have to wait for some time to start another one.
    """
    session_interval = 8

    def __init__(self, user_id):
        """
        To get info of session to make a instance of this class,
        it needs to see the latest session record in db to get id, user_id and so on.
        :param user_id:
        """
        latest_session = models.Session.find_latest_session_data(user_id)

        if latest_session is None:
            self.__id = None
        else:
            self.__id = latest_session['id']
            self.__user_id = latest_session['user_id']
            self.status = latest_session['status']
            self.finish_at = latest_session['finish_at']

    def change_status(self, status: SessionStatus):
        """
        Change the session status.
        To see all status types, refer to /common/constant

        Argument is a Enum
        :param status:
        :return:
        """
        models.Session.update_status(self.id, status)
        self.status = status

    def activate(self):
        """
        To make a session in active status to start CCT.
        :return:
        """
        self.change_status(SessionStatus.active.value)
        self.__update_finish_at()

    def prepare(self):
        """
        When intro finishes, session becomes in prepare state.
        This means session will be activated after one more message.
        :return:
        """
        self.change_status(SessionStatus.prepared.value)

    def __update_finish_at(self):

        new_finish_at = datetime.utcnow() + timedelta(minutes=30)
        models.Session.update_finish_at(self.id, new_finish_at)
        self.finish_at = new_finish_at

    @classmethod
    def __finish_remind_questions(cls, user):
        models.Session.update_latest_session_status(SessionStatus.ended.value, user.id)

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

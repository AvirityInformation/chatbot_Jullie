import models
from common.constant.message_type import MessageType
from common.constant.session_status import SessionStatus
from core.nlp.bot.product.base_bot import BaseBot
from core.nlp.response_generator.factory.cct_response_generator_factory import CCTResponseGeneratorFactory
from db.my_db import MyDB


class FeedbackBot(BaseBot):
    """
    Feedback bot sends message to users who have disappeared during session.
    And ask some questions about users mood.
    """

    def reply(self):
        # this is not good in terms of interface. fix this.
        pass

    def find_inactivated_users(self):
        """
        Find a user who has gone during therapy session.
        :return:
        """
        inactivated_users = models.User.find_inactivated_user_ids()

        return inactivated_users

    def ask_feed_back(self, users: list):
        if not users:
            return

        # response_data = self.create_response(users[0])

        for user_id in users:
            self.send_responses(response_data, user_id)

            self.__change_session_status(user_id)

            print('\n[ASKED COMMENT] User ' + str(user_id))

    # def create_response(self, user):
    #     response_generator = CCTResponseGeneratorFactory.create(user, None, MessageType.ASK_FEED_BACK.value)
    #     response_data = response_generator()
    #
    #     return response_data

    def send_responses(self, response_data, user_id):
        sender_id = models.User.find_sender_id_by_id(user_id)
        MyDB.send_responses(response_data['regular'], None, sender_id,
                            user_id, MessageType.ASK_FEED_BACK.value, should_send_responses_at_once=True)

    def __change_session_status(self, user_id):
        latest_session = models.Session.find_latest_session_data(user_id)
        models.Session.update_status(latest_session['id'], SessionStatus.asking_comment.value)

import logging
import models
from common.constant.message_type import MessageType
from common.util.util import send_typing_on, send_typing_off, send_quick_replies
from core.nlp.bot.product.base_bot import BaseBot
from core.nlp.response_generator.factory.intro_response_generator_factory import IntroResponseGeneratorFactory
from db.my_db import MyDB


class IntroBot(BaseBot):
    """
    This bot gives introduction to users about how client centered therapy works
    When finishing introduction, it creates a session that is in prepared state so that cct bot can
    start session later.
    """

    def __init__(self, user, message):
        self.user = user
        self.message = message
        print('\nintro bot created')

    def reply(self):
        send_typing_on(self.user.sender_id)

        response_data = self.create_response()

        self.send_responses(response_data)

        send_typing_off(self.user.sender_id)

    def create_response(self):
        response_generator = IntroResponseGeneratorFactory.create(self.user, self.message)
        response_data = response_generator()

        return response_data

    def send_responses(self, response_data):
        message_ids = [i['id'] for i in self.message.message_dicts]

        quick_reply_data = response_data['quick_reply']

        should_send_responses_at_once = len(quick_reply_data) != 0
        MyDB.send_responses(response_data['regular'], self.message.cluster_id, self.user.sender_id,
                            self.user.id, MessageType.INTRO.value,
                            should_send_responses_at_once=should_send_responses_at_once)
        print('\nSended regular response\n', response_data['regular'])

        if quick_reply_data:
            models.Response.save_response_data(self.user.id, self.message.cluster_id, quick_reply_data[0],
                                               [quick_reply_data[2]], has_sent=True)
            send_quick_replies(self.user.sender_id, quick_reply_data[0], quick_reply_data[1],
                               quick_reply_data[2])
            print('\nSended quick replies\n', quick_reply_data)

        models.Message.change_message_status(message_ids)

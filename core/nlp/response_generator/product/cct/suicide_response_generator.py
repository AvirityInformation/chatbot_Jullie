import models
from common.constant.payloads import Payload
from common.constant.string_constant import StringConstant
from common.constant.user_status import UserStatus
from core.nlp.response_generator.product.base.base_response_generator import BaseResponseGenerator


class SuicideResponseGenerator(BaseResponseGenerator):
    """
    This class creates response for suicidal messages
    """

    def __call__(self):
        if self.user.status == UserStatus.SUICIDE_IN_SESSION.value:
            return self.__handle_suicidal_user()
        else:
            return self.__give_help_info()

    def __give_help_info(self):
        self.user.update_status(UserStatus.SUICIDE_IN_SESSION.value)

        responses = StringConstant.suicide_responses.value

        quick_reply_data = [
            StringConstant.suicide_quick_replies_title.value,
            StringConstant.suicide_quick_replies.value,
            Payload.SUICIDAL_THOUGHT_DURING_CONVERSATION.value
        ]

        self.set_regular_response(responses)
        self.set_quick_reply(quick_reply_data)

        return self.response_data

    def __handle_suicidal_user(self):
        suicide_quick_replies = StringConstant.suicide_quick_replies.value
        answer = [i['text'] for i in self.message.message_dicts][0]

        if answer == suicide_quick_replies[0]:
            self.response_data = self.__create_ok_response()
        elif answer == suicide_quick_replies[1]:
            self.response_data = self.__create_help_response()
        else:
            self.response_data = self.__create_no_button_response()

        models.Message.change_message_status([i['id'] for i in self.message.message_dicts])

        return self.response_data

    def __create_ok_response(self):
        self.user.update_status(UserStatus.REGULAR.value)

        responses = StringConstant.suicidal_thought_during_conversation_misunderstood.value

        self.set_regular_response(responses)

        return self.response_data

    def __create_help_response(self):
        responses = StringConstant.suicidal_thought_during_conversation_get_help.value

        self.set_regular_response(responses)

        return self.response_data

    def __create_no_button_response(self):
        quick_replies_title = "Can you tell me with the button?"
        quick_replies = StringConstant.suicide_quick_replies.value
        payload = Payload.SUICIDAL_THOUGHT_DURING_CONVERSATION.value

        quick_reply_data = [quick_replies_title, quick_replies, payload]

        self.set_quick_reply(quick_reply_data)

        return self.response_data

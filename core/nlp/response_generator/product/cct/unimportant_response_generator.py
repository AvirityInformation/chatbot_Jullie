from common.constant.intent_type import Intent
from common.constant.string_constant import StringConstant
from core.nlp.response_generator.product.base.base_response_generator import BaseResponseGenerator
import models
from datetime import datetime, timedelta


class UnimportantResponseGenerator(BaseResponseGenerator):
    """
    This class creates responses for unimportant intents like hello.
    """

    def __call__(self):
        response = self.__add_responses_for_unimportant()

        self.set_regular_response(response)

        return self.response_data

    def __add_responses_for_unimportant(self):
        target_intents_list = set([i for i in self.message.intent_list if i.value in Intent.ALL_UNIMPORTANT.value])

        # bye intents comes last. other intents comes first
        normal_intents = [i for i in target_intents_list if
                          i.value not in Intent.NORMAL_AND_UNIMPORTANT.value[4:6]]
        bye_intents = [i for i in target_intents_list if i.value in Intent.NORMAL_AND_UNIMPORTANT.value[4:6]]

        responses = self.__generate_unimportant_type_responses(self.message.intent_list, normal_intents, self.user.id)
        responses += self.__generate_unimportant_type_responses(self.message.intent_list, bye_intents, self.user.id)

        return responses

    @classmethod
    def __generate_unimportant_type_responses(cls, all_intents, target_intents, user_id):
        intent_responses = []
        for i in target_intents:
            if i.value in Intent.UNIMPORTANT_1.value[:4]:  # greetings like hello
                intent_responses = cls.__get_hello_response(user_id, all_intents) + intent_responses
            elif i.value in Intent.UNIMPORTANT_1.value[4:6]:  # bye
                intent_responses += cls.__get_bye_response()
            elif i.value == Intent.UNIMPORTANT_1.value[6]:  # thank you
                intent_responses += cls.__get_thank_response()
            elif i.value == Intent.UNIMPORTANT_1.value[7]:  # there
                intent_responses += cls.__get_there_response()
            elif i.value == Intent.UNIMPORTANT_1.value[8]:  # sorry
                intent_responses += cls.__get_sorry_response()
            elif Intent.NORMAL not in all_intents:
                if i.value == Intent.UNIMPORTANT_2.value[0]:  # no problem
                    intent_responses += cls.__get_no_problem_response()
                elif i.value == Intent.UNIMPORTANT_2.value[1]:  # welcome
                    intent_responses += cls.__get_welcome_response()
                elif i.value == Intent.UNIMPORTANT_2.value[2]:
                    intent_responses += cls.__get_call_jullie_response(all_intents)  # call_jullie
                elif i.value == Intent.UNIMPORTANT_2.value[3]:
                    intent_responses += cls.__get_haha_response()  # haha
                elif i.value == Intent.UNIMPORTANT_2.value[4]:
                    intent_responses += cls.__get_sticker_response()

        return intent_responses

    @classmethod
    def __get_hello_response(cls, user_id, intents):
        has_normal_intent = any(i in {'normal', 'question'} for i in intents)

        if cls.__was_absent_long_time(user_id):

            if has_normal_intent:
                responses = ['Welcome back!!']
            else:
                responses = [
                    'Welcome back!!',
                    'I am happy you come back again!',
                    'What do you want to talk about??'
                ]
        else:
            responses = ['Hey!']

        return responses

    @staticmethod
    def __was_absent_long_time(user_id):
        second_last_message_time = models.Message.find_second_last_message_time(user_id)

        if datetime.utcnow() - second_last_message_time > timedelta(hours=3):
            return True
        else:
            return False

    @staticmethod
    def __get_bye_response():
        return StringConstant.bye_responses.value

    @staticmethod
    def __get_thank_response():
        responses = ['You are welcome :)']
        return responses

    @staticmethod
    def __get_there_response():
        responses = ['i am here :)']
        return responses

    @staticmethod
    def __get_sorry_response():
        responses = [
            'No worry :)',
            'count on me!'
        ]
        return responses

    # >>>>>>>>>>>>>>>>>> UNIMOPRTANT_2 type response_generator
    @staticmethod
    def __get_no_problem_response():
        responses = ['thank you :)']
        return responses

    @staticmethod
    def __get_welcome_response():
        responses = [
            ':)',
            'you are so nice!'
        ]
        return responses

    @staticmethod
    def __get_call_jullie_response(intents):
        if any(i.value in Intent.UNIMPORTANT_1.value[:4] for i in intents):
            responses = [
                'I am right here!',
                'What happened??'
            ]
        else:
            responses = [
                'Hey!',
                'I am right here!',
                'What happened??'
            ]

        return responses

    @staticmethod
    def __get_haha_response():
        return ['haha']

    @staticmethod
    def __get_sticker_response():
        responses = [
            'You know i am always here for you'
        ]

        return responses

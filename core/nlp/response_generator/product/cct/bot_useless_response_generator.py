import numpy as np
from common.constant.string_constant import StringConstant
from core.nlp.response_generator.product.base.base_response_generator import BaseResponseGenerator


class BotUselessResponseGenerator(BaseResponseGenerator):
    """
    This class creates responses for users saying that bot is useless or helpless
    """

    def __call__(self):
        responses = self.__select_responses_for_complaint()

        self.response_data['regular'] = responses

        return self.response_data

    @staticmethod
    def __select_responses_for_complaint():
        responses_options = StringConstant.response_options_for_complaint.value
        np.random.shuffle(responses_options)

        return responses_options[0]

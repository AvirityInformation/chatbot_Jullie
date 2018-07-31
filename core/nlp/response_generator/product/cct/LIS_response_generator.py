import numpy as np
from common.constant.df_from_csv import LISTENING_DF
from core.nlp.response_generator.product.base.base_response_generator import BaseResponseGenerator


class LISResponseGenerator(BaseResponseGenerator):
    """
    This class creates 'listening' responses
    """

    def __call__(self):
        responses = self.generate_listening()

        self.response_data['regular'] = responses

        return self.response_data

    @staticmethod
    def generate_listening():
        listening = LISTENING_DF[LISTENING_DF.type == 1].text.values
        response_list = [np.random.choice(listening, 1)[0]]
        return response_list

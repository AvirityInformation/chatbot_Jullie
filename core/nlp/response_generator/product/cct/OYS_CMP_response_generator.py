from core.nlp.response_generator.product.base.base_response_generator import BaseResponseGenerator
import numpy as np


class OYSCMPResponseGenerator(BaseResponseGenerator):
    """
    This class creates OYS(On Your Side) and Cmp(Compassion) responses
    """

    def __call__(self):
        responses = self.__create_oys_after_cmp()

        self.response_data['regular'] = responses

        return self.response_data

    def __create_oys_after_cmp(self):
        options = [
            ["Life is tough😞", "I am here for you now"],
            ["I am sorry for you..😢", "Just vent me anything you want"],
            ["Life is not always easy right☹️", "Let me just be with you"]
        ]

        np.random.shuffle(options)

        return options[0]

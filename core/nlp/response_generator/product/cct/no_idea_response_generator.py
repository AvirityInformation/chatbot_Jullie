import numpy as np
from common.constant.string_constant import StringConstant
from core.nlp.response_generator.product.base.base_response_generator import BaseResponseGenerator


class NoIdeaResponseGenerator(BaseResponseGenerator):
    """
    This class creates responses for users who have no idea what to do
    """

    def __call__(self):
        responses = np.random.choice(StringConstant.guess_advise_list.value, 1)[0]

        self.response_data['regular'] = responses

        return self.response_data

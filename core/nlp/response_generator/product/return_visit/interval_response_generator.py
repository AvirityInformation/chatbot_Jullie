from common.constant.string_constant import StringConstant
from core.nlp.response_generator.product.base.base_response_generator import BaseResponseGenerator


class IntervalResponseGenerator(BaseResponseGenerator):
    """
    This class tells users that they have to wait until session interval ends
    """

    def __call__(self, *args):
        responses = StringConstant.interval_responses.value

        self.set_regular_response(responses)

        return self.response_data

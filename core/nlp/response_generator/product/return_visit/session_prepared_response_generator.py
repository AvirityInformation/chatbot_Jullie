from core.nlp.response_generator.product.base.base_response_generator import BaseResponseGenerator


class SessionPreparedResponseGenerator(BaseResponseGenerator):
    """
    This class creates responses for preppared sessions.
    """
    def __call__(self):
        responses = [
            "Sure!",
            "Tell me what you have in your mind :)"
        ]

        self.set_regular_response(responses)

        return self.response_data

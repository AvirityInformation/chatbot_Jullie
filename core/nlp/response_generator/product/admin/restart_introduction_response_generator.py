from core.nlp.response_generator.product.base.base_response_generator import BaseResponseGenerator
from scripts.delete_user_from_db import delete_all_rows_of_a_user


class RestartIntroductionResposneGenerator(BaseResponseGenerator):
    """
    This class deal with admin command RESTART_INTRODUCTION
    """
    def __call__(self):
        delete_all_rows_of_a_user(self.user.id, from_messenger=True)

        return self.response_data

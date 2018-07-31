from common.constant.intent_type import Intent
from core.nlp.response_generator.product.base.base_response_generator import BaseResponseGenerator
from core.nlp.question import question


class GeneralQuestionResponseGenerator(BaseResponseGenerator):
    """
    This question make responses for general questions.
    """

    def __call__(self):
        question_sidx = [idx for idx, i in enumerate(self.message.intent_list) if i == Intent.QUESTION_GENERAL_TYPE]

        q_sent = self.message.text_df[self.message.text_df.sidx.isin(question_sidx)]
        question_type = question.DefineQuestionType(q_sent).categorize_by_leading_word()

        responses = question_type.answer

        self.response_data['regular'] = responses

        return self.response_data

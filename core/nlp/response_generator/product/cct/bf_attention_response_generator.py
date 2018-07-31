from random import randint
from core.nlp.response_generator.product.base.base_response_generator import BaseResponseGenerator


class BfAttentionResponseGenerator(BaseResponseGenerator):
    """
    This class deals with messages that mean user wants to get bf's attention
    """

    def __call__(self):
        responses = self.__create_response_for_cant_get_attention_from_bf()

        self.set_regular_response(responses)
        return self.response_data

    @classmethod
    def __create_response_for_cant_get_attention_from_bf(cls):
        qr = cls.__create_qr_response()

        cmp_list = cls.__create_cmp_response()

        guess_list = cls.__create_guess_response()

        random_idx_for_cmp_list = randint(0, len(cmp_list) - 1)
        random_idx_for_guess_list = randint(0, len(guess_list) - 1)

        return qr + cmp_list[random_idx_for_cmp_list] + guess_list[
            random_idx_for_guess_list]

    @classmethod
    def __create_qr_response(cls):
        qr_list = [
            ["i am sorry to hear that"],
            ["omg.."],
            ["im sorry"],
            ["jeez.."],
            ["okay"]
        ]

        random_idx_for_qr_list = randint(0, len(qr_list) - 1)

        qr = qr_list[random_idx_for_qr_list]

        return qr

    @classmethod
    def __create_cmp_response(cls):
        adj_hard_list = ["difficult", "hard", "tough", "painful", "rough"]

        random_idx_for_adj_hard = randint(0, len(adj_hard_list) - 1)

        adj_hard = adj_hard_list[random_idx_for_adj_hard]

        cmp_list = [
            ["i know waiting til he answers is so " + adj_hard + "😢"],
            ["its just so " + adj_hard + " to wait til he comes back to you right😓"],
            ["sounds " + adj_hard + " time for you til he will reach out to you😥"],
            ["i know its " + adj_hard + " that he doesnt pay attention to you😞"]
        ]

        return cmp_list

    @classmethod
    def __create_guess_response(cls):
        emotion_adj_list = ["anxious", "stressed", "uneasy", "insecure", "worried"]
        emotion_noun_list = ["anxiety", "stress", "uneasiness", "insecurity", "worry"]

        random_idx_for_emotion_adj = randint(0, len(emotion_adj_list) - 1)
        random_idx_for_emotion_noun = randint(0, len(emotion_noun_list) - 1)

        emotion_adj = emotion_adj_list[random_idx_for_emotion_adj]
        emotion_noun = emotion_noun_list[random_idx_for_emotion_noun]

        guess_list = [
            ["it can give you major " + emotion_noun],
            ["it could make you feel like " + emotion_adj],
            ["you could feel like " + emotion_adj],
            ["could give you little " + emotion_noun]
        ]

        return guess_list

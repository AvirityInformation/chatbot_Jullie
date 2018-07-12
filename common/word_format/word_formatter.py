from nltk import word_tokenize, sent_tokenize
import logging


class WordFormatter:
    """
    This is utils class to convert word formats
    """

    @staticmethod
    def wtoks2str(w_toks):
        """
        :param w_toks: list [['i', 'am', 'sad'],['thank','you]]
        :return: str "i am sad. thank you."
        """

        if not w_toks:
            return w_toks

        text = ''
        for idx, sent in enumerate(w_toks):
            if idx == 0:
                text = WordFormatter.wtok2str(sent)
            else:
                text += ' ' + WordFormatter.wtok2str(sent)

        return text

    @staticmethod
    def wtok2str(w_tok):
        """
        :param w_tok: ['i', 'am', 'sad']
        :return: str: "i am sad."
        """
        if not w_tok:
            return w_tok

        result = ''.join(
            '' if word == ''
            else ' ' + str(word) if all(c.isdigit() for c in word)
            else str(word) if all(not c.isalpha() for c in word)
            else ' ' + str(word) + '.' if widx == len(w_tok) - 1 and any(c.isalpha() for c in word)
            else word if widx == 0
            else ' ' + str(word)
            for widx, word in enumerate(w_tok)
        )

        return result

    @staticmethod
    def stoks2wtoks(s_toks):
        try:
            return [word_tokenize(s) for s in s_toks]
        except Exception:
            logging.exception('Error at: ' + str(__name__))
            return [[]]

    @staticmethod
    def df2wtoks(text_df, column_name="word"):
        try:
            if text_df is None:
                return []

            w_toks = []
            for idx, sidx in enumerate(list(set(text_df.sidx.tolist()))):
                w_toks.append([])

                for word in text_df.loc[text_df.sidx == sidx, column_name].tolist():
                    w_toks[idx].append(word)

            return w_toks
        except Exception:
            logging.exception('Error at: ' + str(__name__))
            return [[]]

    @staticmethod
    def Df2Str(text_df):
        try:
            w_toks = WordFormatter.df2wtoks(text_df)

            text = WordFormatter.wtoks2str(w_toks)

            return text
        except Exception:
            logging.exception('Error at: ' + str(__name__))
            return ''

    @staticmethod
    def Series2Str(series):
        try:
            return " ".join([word for word in series])
        except Exception:
            logging.exception('Error at: ' + str(__name__))
            return ''

    @staticmethod
    def MsgDict2WToks(message_dicts):
        try:
            s_toks = [d['text'] for d in message_dicts]
            w_toks = WordFormatter.stoks2wtoks(s_toks)

            return w_toks
        except Exception:
            logging.exception('Error at: ' + str(__name__))
            return [[]]

    @staticmethod
    def Str2WToks(text):
        try:
            s_toks = sent_tokenize(text)
            w_toks = [word_tokenize(s) for s in s_toks]

            return w_toks
        except Exception:
            logging.exception('Error at: ' + str(__name__))
            return [[]]

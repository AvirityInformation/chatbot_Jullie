from nltk import word_tokenize, sent_tokenize
import logging

# class for convert among df, w_toks, s_toks and regular text
class WordFormatter:
    @staticmethod
    def WToks2Str(w_toks):
        text = ''
        if len(w_toks) != 0:
            for sent in w_toks:
                text += WordFormatter.SingleWToks2Str(sent)

            return text
        else:
            return text

    @staticmethod
    def SingleWToks2Str(w_tok):
        if len(w_tok) != 0:
            return ''.join(
                '' if word == ''
                else ' ' + str(word) if all(c.isdigit() for c in word)
                else str(word) if all(not c.isalpha() for c in word)
                else ' ' + str(word) + '.' if widx == len(w_tok) - 1 and any(c.isalpha() for c in word)
                else ' ' + str(word)
                for widx, word in enumerate(w_tok)
            )
        else:
            return ''

    @staticmethod
    def SToks2WToks(s_toks):
        if len(s_toks) != 0:
            return [word_tokenize(s) for s in s_toks]
        else:
            return [[]]

    @staticmethod
    def Df2WToks(text_df, column_name="word"):
        if text_df is None:
            return []

        w_toks = []
        for idx, sidx in enumerate(list(set(text_df.sidx.tolist()))):
            w_toks.append([])

            for word in text_df.loc[text_df.sidx == sidx, column_name].tolist():
                w_toks[idx].append(word)

        return w_toks


    @staticmethod
    def Df2Str(text_df):
        w_toks = WordFormatter.Df2WToks(text_df)

        text = WordFormatter.WToks2Str(w_toks)

        return text


    @staticmethod
    def Series2Str(series):
        if len(series) != 0:
            return " ".join([word for word in series])
        else:
            return ''

    @staticmethod
    def MsgDict2WToks(message_dicts):
        if len(message_dicts) != 0:
            s_toks = [d['text'] for d in message_dicts]
            w_toks = WordFormatter.SToks2WToks(s_toks)

            return w_toks
        else:
            return [[]]

    @staticmethod
    def Str2WToks(text):
        if len(text) != 0:
            s_toks = sent_tokenize(text)
            w_toks = [word_tokenize(s) for s in s_toks]

            return w_toks
        else:
            return [[]]

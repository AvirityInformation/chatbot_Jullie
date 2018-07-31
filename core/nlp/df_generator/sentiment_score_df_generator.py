import pandas as pd
import numpy as np


class SentimentScoreDFGenerator:
    """
    sentiment score is a df with negative/positive score of each sentence
    This class must be integrated to preprocessor
    """

    def __call__(self, text_df: pd.DataFrame, text_kw_df: pd.DataFrame):
        """
        this method creates a df containing positive/negative score of each sentence.

        :param text_df:
        :param text_kw_df:
        :return:
        """
        if text_df is None:
            return None

        if text_kw_df is None:
            sentiment_score_df = pd.DataFrame({"sidx": text_df.sidx.tolist()})
            sentiment_score_df['nscore'] = 0
            sentiment_score_df['pscore'] = 0

            return sentiment_score_df

        # get the sentiment score sscore of each sentence.
        npdf = self.__sum_sentiment_scores(text_df, text_kw_df)
        sentiment_score_df = npdf.iloc[:, 0:3]

        print("\nSentiment score df\n{}".format(sentiment_score_df))

        return sentiment_score_df

    @classmethod
    def __get_kwscores(cls, text_df, text_kw_df):
        kwscore_df = pd.DataFrame(list(set(text_df.sidx)))

        kwscore_df['sent_score'] = 0

        kwscore_df.sent_score = kwscore_df.apply(
            lambda row: sum([i for i in text_kw_df[text_kw_df.sidx == row.name].iscore]), axis=1
        )

        kwscore_df = kwscore_df.astype(object).replace(np.nan, 0.0)

        kwscore_df['order_bonus'] = cls.__get_order_bonus(text_df)

        kwscore_df['sent_kwscore'] = kwscore_df.sent_score * kwscore_df.order_bonus
        return kwscore_df

    @classmethod
    def __sum_sentiment_scores(cls, text_df, text_kw_df):
        # calculate for both negative and positive
        npdf = pd.DataFrame({'sidx': list(set(text_df.sidx))})

        npdf['nscore'] = 0
        npdf['pscore'] = 0
        # it used to only get the word belongs to subject "i" but temporary simplify it
        for ridx, row in text_kw_df.iterrows():
            if row.sscore > 0:
                npdf.pscore[row.sidx] += row.sscore
            else:
                npdf.nscore[row.sidx] += row.sscore

        return npdf

    @staticmethod
    def __get_order_bonus(text_df):
        num_of_sentences = len(set(text_df.sidx.values))
        if num_of_sentences == 0:
            return [1]

        margin = 0.5 / num_of_sentences

        order_bonus = [1 + i * margin for i in range(0, num_of_sentences)]

        return order_bonus

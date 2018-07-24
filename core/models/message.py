import logging
import models


class Message:
    """
    This class has information of message user sent.
    """

    def __init__(self, message_dicts, user_id, is_nlp_skipped=False):
        """
        Each instance of this class represent for a CLUSTER that is a combination of some messages sent by users.
        If the message is during the session, the instance will have session_id too.
        :param message_dicts:
        :param user_id:
        :param is_nlp_skipped:
        """
        self.message_dicts = message_dicts
        self.__cluster_id = models.Message.find_cluster_id(message_dicts)
        self.__session_id = models.Session.find_latest_id_by_user_id(user_id)

        if is_nlp_skipped:
            return

        self.__original_df = None
        self.__text_df = None
        self.__intent_list = None
        self.__text_kw_df = None
        self.__sentiment_score_df = None

    def mark_done(self):
        """
        This function change the status of message in db so that the messages won't be handled again.
        :return:
        """
        message_ids = [i['id'] for i in self.message_dicts]
        models.Message.change_message_status(message_ids)
        print('\nmessage done')

    @property
    def cluster_id(self):
        return self.__cluster_id

    @property
    def session_id(self):
        return self.__session_id

    @property
    def original_df(self):
        return self.__original_df

    @original_df.setter
    def original_df(self, original_df):
        self.__original_df = original_df

    @property
    def text_df(self):
        return self.__text_df

    @text_df.setter
    def text_df(self, text_df):
        self.__text_df = text_df

    @property
    def intent_list(self):
        return self.__intent_list

    @intent_list.setter
    def intent_list(self, intent_list):
        self.__intent_list = intent_list

    @property
    def text_kw_df(self):
        return self.__text_kw_df

    @text_kw_df.setter
    def text_kw_df(self, text_kw_df):
        self.__text_kw_df = text_kw_df

    @property
    def sentiment_score_df(self):
        return self.__sentiment_score_df

    @sentiment_score_df.setter
    def sentiment_score_df(self, sentiment_score_df):
        self.__sentiment_score_df = sentiment_score_df

from abc import ABC, abstractmethod


class BaseBot(ABC):
    """
    This works as an interface class.
    Every bot class needs to overide this base class.
    This has 3 abstractmethod so all overiding classes needs to have those methods.
    """
    @abstractmethod
    def reply(self, *arguments):
        """
        Receive response text from create_response function and send it to users by send_responses function.
        :param arguments:
        :return:
        """
        pass

    @abstractmethod
    def create_response(self, *arguments):
        """
        Make response texts
        :param arguments:
        :return:
        """
        pass

    @abstractmethod
    def send_responses(self, *arguments):
        """
        Send responses to facebook send api
        :param arguments:
        :return:
        """
        pass

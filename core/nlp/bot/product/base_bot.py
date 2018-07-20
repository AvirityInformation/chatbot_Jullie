from abc import ABC, abstractmethod


class BaseBot(ABC):
    """
    This works as an interface class.
    Every bot class needs to overide this base class.
    This has 3 abstractmethod so all overiding classes needs to have those methods.
    """
    @abstractmethod
    def reply(self, *arguments):
        pass

    @abstractmethod
    def create_response(self, *arguments):
        pass

    @abstractmethod
    def send_responses(self, *arguments):
        pass

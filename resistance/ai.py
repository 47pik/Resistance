import abc


class AI:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def choose_vote(self):
        """
        Returns True if choose to approve mission, returns False if choose to reject
        """
        return

    @abc.abstractmethod
    def choose_mission_team(self):
        """
        Returns a list of Players to send on a mission
        """
        return

    @abc.abstractmethod
    def choose_mission_card(self):
        """
        Returns True if choose to succeed mission, returns False if choose to fail
        """
        return
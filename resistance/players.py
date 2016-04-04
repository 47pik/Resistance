import abc


class Player:
    __metaclass__ = abc.ABCMeta

    def __init__(self, ai):
        self.__ai = ai
        pass

    def vote(self):
        return self.__ai.choose_vote()

    @abc.abstractmethod
    def choose_mission_card(self):
        pass


class Resistance(Player):

    def __init__(self):
        Player.__init__()

    def choose_mission_card(self):
        return True


class Spy(Player):

    def __init__(self):
        Player.__init__()

    def choose_mission_card(self):
        return self.__ai.choose_mission_card()
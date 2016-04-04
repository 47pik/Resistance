class Game:

    def __init__(self, players):

        if players > 10 or players < 5:
            raise InputError('invalid number of players')

        if players == 5:
            self.__missions = [2, 3, 2, 3, 3]
        elif players == 6:
            self.__missions = [2, 3, 4, 3, 4]
        elif players == 7:
            self.__missions = [2, 3, 3, 4, 4]
        else:
            self.__missions = [3, 4, 4, 5, 5]

        if players >= 7:
            self.__fails_required = [1, 1, 1, 2, 1]
        else:
            self.__fails_required = [1, 1, 1, 1, 1]

        self.__mission_results = []     # 'R' indicates Resistance, 'S' indicates Spies
        self.__mission_idx = 0
        self.__round = 0

        self.__players = [Player() for i in range(players)]
        self.__leader_idx = 0

    def round_number(self):
        return self.__round + 1

    def current_mission(self):
        return self.__mission_idx + 1

    def mission_leader(self):
        return self.__players[self.__leader_idx]

    def players(self):
        return self.__players


class InputError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        msg  -- explanation of the error
    """
    def __init__(self, msg):
        self.msg = msg
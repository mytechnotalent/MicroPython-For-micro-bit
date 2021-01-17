from Player import Player


class EscapeRoomPlayer(Player):
    """
    Child class to represent an escape room player inheriting from the Player base class
    """

    def __init__(self, name=None, __dx=1, __dy=1, armour=None, inventory=None):
        """
        Attrs:
            name: str
            __dx: int
            __dy: int
            armour = list
            inventory: list
        """
        super().__init__(name, __dx, __dy, armour, inventory)

    def reset_player_location(self):
        """
        Method to move an escape room player to init position after an incorrect answer

        Returns:
            tuple
        """
        self.__dx = 1
        self.__dy = 1
        return self.__dx, self.__dy

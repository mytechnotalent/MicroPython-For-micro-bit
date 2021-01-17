class Player:
    """
    Base class to represent a generic player
    """

    def __init__(self, name='Generic', __dx=0, __dy=0, armour=None, inventory=None):
        """
        Attrs:
            name: str
            __dx: int
            __dy: int
            armour = list
            inventory: list
        """
        self.name = name
        self.__dx = __dx
        self.__dy = __dy
        if armour is None:
            armour = []
        self.armour = armour
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def __move(self, dx, dy):
        """Method to move a generic player based on their current x and y location

        Params:
            dx: int
            dy: int
        """
        self.__dx += dx
        self.__dy += dy

    def move_north(self):
        """
        Method to move a generic player from their current position to one position north
        """
        self.__move(dx=0, dy=-1)

    def move_south(self):
        """
        Method to move a generic player from their current position to one position south
        """
        self.__move(dx=0, dy=1)

    def move_east(self):
        """
        Method to move a generic player from their current position to one position east
        """
        self.__move(dx=1, dy=0)

    def move_west(self):
        """
        Method to move a generic player from their current position to one position west
        """
        self.__move(dx=-1, dy=0)

    def location(self):
        """
        Method to return a generic players current position

        Returns:
            tuple
        """
        return self.__dx, self.__dy

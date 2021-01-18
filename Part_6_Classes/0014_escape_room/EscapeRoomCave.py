from Room import Room


class EscapeRoomCave(Room):
    """
    Child class to represent an escape room cave inheriting from the
    Room base class
    """

    def __init__(self, led_height, led_width):
        """
        Attrs:
            led_height: int
            led_width: int
        """
        super().__init__(led_height, led_width)

    def grid_size(self):
        """
        Method to return a cave room grid

        Returns:
            int, int
        """
        led_height, led_width = super(EscapeRoomCave, self).grid_size()
        return led_height, led_width

    def __optional_spaces(self):
        """
        Method to obtain remaining spaces on micro:bit display

        Returns:
             str, str
        """
        led_height, led_width = self.grid_size()
        return led_height-2, led_width-2

    def optional_spaces_available(self):
        """
        Determine optional spaces escape room player can move in order to keep
        escape room player from going out of bounds of the cave walls

        Returns:
             int, int
        """
        optional_height, optional_width = self.__optional_spaces()
        return optional_height, optional_width

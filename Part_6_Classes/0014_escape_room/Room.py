class Room:
    """
    Base class to represent a generic room
    """

    def __init__(self, led_height=0, led_width=0):
        """
        Attrs:
            led_height: int
            led_width: int
        """
        self.led_height = led_height
        self.led_width = led_width

    def grid_size(self):
        """
        Method to return a generic room grid

        Returns:
            int, int
        """
        return self.led_height, self.led_width

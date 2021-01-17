class Ui:
    """
    Base class to implement a generic user interface
    """

    def __init__(self, interface=None):
        """
        Attrs:
            interface: str
        """
        self.interface = interface

    @staticmethod
    def intro():
        """
        Method to give a generic intro
        """
        intro_text = '\nWelcome to generic!\n'
        intro_text += 'Generic instructions.\n'
        return intro_text

    @staticmethod
    def draw_grid(led_height, led_width, led_on, led_off):
        """
        Method to draw grid on generic led display

        Params:
            led_height: int
            led_width: int
            led_on: str
            led_off: str

        Returns:
             str, str, str
        """
        top_wall = led_on * led_width + '\n'
        side_walls = ''
        for _ in range(led_height - 2):
            # noinspection PyTypeChecker
            side_walls += led_on + led_off * (led_width - 2) + led_on + '\n'
        bottom_wall = led_on * led_width
        return top_wall, side_walls, bottom_wall

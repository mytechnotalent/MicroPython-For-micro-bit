from microbit import display, Image
from Ui import Ui


class EscapeRoomUi(Ui):
    """
    Child class to handle the escape room user interface from the
    Ui base class
    """

    def __init__(self, interface=None):
        """
        Attrs:
            interface: str
        """
        super().__init__(interface)

    @staticmethod
    def intro():
        """
        Method to handle escape room intro
        """
        intro_text_welcome = '\nWelcome to the Escape Room Game!\n'
        intro_speaking_instructions = 'Press the buttons, logo and pin zero to move.\n'
        return intro_text_welcome, intro_speaking_instructions

    def update_display(self, led_height, led_width, player_location):
        """
        Update display with each event where we re-draw
        cave and player's current position
        """
        display.clear()
        top_wall, side_walls, bottom_wall = super(EscapeRoomUi, self).draw_grid(led_height, led_width, '9', '0')
        grid = top_wall + side_walls + bottom_wall
        display.show(Image(grid))
        display.set_pixel(player_location[0], player_location[1], 9)

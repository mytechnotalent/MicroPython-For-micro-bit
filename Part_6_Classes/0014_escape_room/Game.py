from time import sleep
from microbit import display, Image, button_a, pin_logo, button_b
from speech import say
import music


class Game:
    """
    Class to handle game logic
    """

    def __init__(self, optional_height=0, optional_width=0, led_height=0, led_width=0, player_location=None,
                 speech_speed=95):
        """
        Attrs:
            optional_height: int
            optional_width: int
            led_height: int
            led_width: int
            player_location: tuple
            speech_speed: int
        """
        self.optional_height = optional_height
        self.optional_width = optional_width
        self.led_height = led_height
        self.led_width = led_width
        self.player_location = player_location
        self.speech_speed = speech_speed

    def __redraw_screen(self, player, ui):
        """
        Method to handle redrawing screen

        Params:
            player: object
            ui: object
        """
        self.player_location = player.location()
        display.clear()
        grid = ui.update_display(self.led_height, self.led_width)
        display.show(Image(grid))
        display.set_pixel(self.player_location[0], self.player_location[1], 9)

    def init(self, cave, player, ui):
        """
        Method to game initialization

        Params:
            cave: object
            player: object
            ui: object

        Return:
            int, int
        """
        self.optional_height, self.optional_width = cave.optional_spaces_available()
        self.led_height, self.led_width = cave.grid_size()
        self.player_location = player.location()
        display.clear()
        grid = ui.update_display(self.led_height, self.led_width)
        display.show(Image(grid))
        display.set_pixel(self.player_location[0], self.player_location[1], 9)
        intro_text_welcome, intro_speaking_instructions = ui.intro()
        say(intro_text_welcome, speed=self.speech_speed)
        say(intro_speaking_instructions, speed=self.speech_speed)

    def update_screen(self, player, ui):
        """
        Method to handle redrawing screen

        Params:
            player: object
            ui: object
        """
        player.reset_player_location()
        self.__redraw_screen(player, ui)

    def button_a_press(self, player, ui):
        """
        Method to handle a button_a press

        Params:
            player: object
            ui: object

        Returns:
            tuple
        """
        # If badge player is against the left wall do NOT allow them to go through it
        if self.player_location[0] != 1 and self.player_location[0] <= self.optional_width:
            player.move_west()
            self.__redraw_screen(player, ui)
        sleep(0.25)
        return self.player_location

    def button_b_press(self, player, ui):
        """
        Method to handle a button_b press

        Params:
            player: object
            ui: object

        Returns:
            tuple
        """
        if self.player_location[0] < self.optional_width:
            player.move_east()
            self.__redraw_screen(player, ui)
        sleep(0.25)
        return self.player_location

    def pin_logo_press(self, player, ui):
        """
        Method to handle a pin_logo press

        Params:
            player: object
            ui: object

        Returns:
            tuple
        """
        # If badge player is against the top wall do NOT allow them to go through it
        if self.player_location[1] != 1 and self.player_location[1] <= self.optional_height:
            player.move_north()
            self.__redraw_screen(player, ui)
        sleep(0.25)
        return self.player_location

    def pin2_press(self, player, ui):
        """
        Method to handle a pin2 press

        Params:
            player: object
            ui: object

        Returns:
            tuple
        """
        if self.player_location[1] < self.optional_height:
            player.move_south()
            self.__redraw_screen(player, ui)
        sleep(0.25)
        return self.player_location

    @staticmethod
    def get_inventory(player, file_manager):
        """
        Method to get the inventory from disk
        """
        inventory = file_manager.read_inventory_file()
        player.inventory.append(inventory)

    def ask_question(self, question):
        """
        Method to handle ask question logic

        Params:
            question: object

        Returns:
             int, int, str
        """
        random_question, answer_1, answer_2, answer_3, correct_answer_index, correct_answer \
            = question.get_random_question()
        say(random_question, speed=self.speech_speed)
        say('Press Ayy for {0}.'.format(answer_1), speed=self.speech_speed)
        say('Toch the logo for {0}.'.format(answer_2), speed=self.speech_speed)
        say('Press B for {0}.'.format(answer_3), speed=self.speech_speed)
        while True:
            if button_a.is_pressed():
                response = 0
                break
            elif pin_logo.is_touched():
                response = 1
                break
            elif button_b.is_pressed():
                response = 2
                break
        return response, correct_answer_index, correct_answer

    def correct_answer_response(self, sound_effects):
        """
        Method to handle correct answer logic

        Params:
            sound_effects: object
        """
        say('Correct!', speed=self.speech_speed)
        sound_effects.play_success_sound_effect()

    def picked_up_red_key(self, file_manager):
        """
        Method to handle picking up red key

        Params:
            file_manager: object
        """
        file_manager.write_inventory_file()
        say('You picked up the red key!', speed=self.speech_speed)

    def incorrect_answer_response(self, correct_answer):
        """
        Method to handle correct answer logic

        Params:
            correct_answer: str
        """
        say('The correct answer is {0}.'.format(correct_answer), speed=self.speech_speed)

    def win(self, sound_effects, file_manager):
        """
        Method to handle win game logic

        Params:
            sound_effects: object
            file_manager: object
        """
        file_manager.clear_inventory_file()
        say('You Won!  You Escaped!', speed=self.speech_speed)
        win_game_sound_effect = sound_effects.win_game_sound_effect()
        music.play(win_game_sound_effect)
        display.show(Image.ALL_CLOCKS, loop=True, delay=100)

    def without_red_key(self):
        """
        Method to handle not having the red key logic
        """
        say('You do not have the red key to escape.', speed=self.speech_speed)

from time import sleep
from microbit import display, Image, button_a, button_b, pin_logo, pin2
from Speech import Speech
from EscapeRoomCave import EscapeRoomCave
from EscapeRoomPlayer import EscapeRoomPlayer
from EscapeRoomUi import EscapeRoomUi
from EscapeRoomSoundEffects import EscapeRoomSoundEffects
from Question import Question
from FileManager import FileManager

speech = Speech()
cave = EscapeRoomCave(5, 5)
player = EscapeRoomPlayer()
ui = EscapeRoomUi()
question = Question()
sound_effects = EscapeRoomSoundEffects()
file_manager = FileManager()

if __name__ == '__main__':
    optional_height, optional_width = cave.optional_spaces_available()
    led_height, led_width = cave.grid_size()
    player_location = player.location()
    ui.update_display(led_height, led_width, player_location)
    intro_text_welcome, intro_speaking_instructions = ui.intro()
    speech.speak(intro_text_welcome)
    speech.speak(intro_speaking_instructions)

    question_1 = False
    final_question = False

    while True:
        if button_a.is_pressed():
            # If badge player is against the left wall do NOT allow them to go through it
            if player_location[0] != 1 and player_location[0] <= optional_width:
                player.move_west()
                player_location = player.location()
                ui.update_display(led_height, led_width, player_location)
            sleep(0.25)
        if button_b.is_pressed():
            if player_location[0] < optional_width:
                player.move_east()
                player_location = player.location()
                ui.update_display(led_height, led_width, player_location)
            sleep(0.25)
        if pin_logo.is_touched():
            # If badge player is against the top wall do NOT allow them to go through it
            if player_location[1] != 1 and player_location[1] <= optional_height:
                player.move_north()
                player_location = player.location()
                ui.update_display(led_height, led_width, player_location)
            sleep(0.25)
        if pin2.is_touched():
            if player_location[1] < optional_height:
                player.move_south()
                player_location = player.location()
                ui.update_display(led_height, led_width, player_location)
            sleep(0.25)
        if player_location == (2, 2) and not question_1:
            inventory = file_manager.read_inventory_file()
            player.inventory.append(inventory)
            if 'Red Key' not in player.inventory:
                question_1 = question.ask()
                if question_1:
                    player.inventory.append('Red Key')
                    speech.speak('You picked up the red key!')
                    file_manager.write_inventory_file()
                if not question_1:
                    question_1 = False
                    player_location = player.reset_player_location()
                    ui.update_display(led_height, led_width, player_location)
        if player_location == (3, 1) and not final_question:
            inventory = file_manager.read_inventory_file()
            player.inventory.append(inventory)
            final_question = question.ask()
            if final_question:
                if 'Red Key' in player.inventory:
                    speech.speak('You Won!  You Escaped!')
                    sound_effects.win_game_sound_effect()
                    file_manager.clear_inventory_file()
                    display.show(Image.ALL_CLOCKS, loop=True, delay=100)
                else:
                    speech.speak('You do not have the red key to escape.')
                    final_question = False
            if not final_question:
                final_question = False
                player_location = player.reset_player_location()
                ui.update_display(led_height, led_width, player_location)

from microbit import button_a, button_b, pin_logo, pin2
from EscapeRoomCave import EscapeRoomCave
from EscapeRoomPlayer import EscapeRoomPlayer
from EscapeRoomUi import EscapeRoomUi
from EscapeRoomSoundEffects import EscapeRoomSoundEffects
from Question import Question
from FileManager import FileManager
from RandomNumberGenerator import RandomNumberGenerator
from Game import Game

cave = EscapeRoomCave(5, 5)
player = EscapeRoomPlayer()
ui = EscapeRoomUi()
question = Question()
sound_effects = EscapeRoomSoundEffects()
file_manager = FileManager()
random_number_generator = RandomNumberGenerator()
game = Game()

if __name__ == '__main__':
    game.init(cave, player, ui)

    player_location = (0, 0)

    question_1 = False
    final_question = False

    while True:
        if button_a.is_pressed():
            player_location = game.button_a_press(player, ui)
        if button_b.is_pressed():
            player_location = game.button_b_press(player, ui)
        if pin_logo.is_touched():
            player_location = game.pin_logo_press(player, ui)
        if pin2.is_touched():
            player_location = game.pin2_press(player, ui)

        x, y = random_number_generator.generate_random_numbers()
        if player_location == (x, y) and not question_1:
            game.get_inventory(player, file_manager)
            if 'Red Key' not in player.inventory:
                response, correct_answer_index, correct_answer = game.ask_question(question)
                if response == correct_answer_index:
                    game.correct_answer_response(sound_effects)
                    game.picked_up_red_key(file_manager)
                    question_1 = True
                else:
                    game.incorrect_answer_response(correct_answer)
                game.update_screen(player, ui)

        x, y = random_number_generator.generate_random_numbers()
        if player_location == (x, y) and not final_question:
            game.get_inventory(player, file_manager)
            response, correct_answer_index, correct_answer = game.ask_question(question)
            if response == correct_answer_index:
                game.correct_answer_response(sound_effects)
                final_question = True
            else:
                game.incorrect_answer_response(correct_answer)
            if 'Red Key' in player.inventory and final_question:
                game.win(sound_effects, file_manager)
                break
            elif final_question:
                game.without_red_key()
            game.update_screen(player, ui)

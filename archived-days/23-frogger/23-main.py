import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def reset_game():
    global reset_state
    reset_state = True


screen = Screen()
level = 1
reset_state = False
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkeypress(player.move, "Up")
screen.onkeypress(reset_game, "space")
scoreboard = Scoreboard()
car_manager = CarManager()

running = True
game_is_on = True
while running:
    while game_is_on:
        time.sleep(0.1)
        if car_manager.update_screen(level, player):
            game_is_on = False
        elif player.detect_edge():
            level += 1
        scoreboard.set_level(level)
        screen.update()

    scoreboard.kill_screen()
    if reset_state:
        level = 1
        player.reset()
        car_manager.clear_manager(screen)
        scoreboard.clear_killscreen()
        game_is_on = True
        reset_state = False





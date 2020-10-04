from maze import Maze
from player import Player


class Game:

    def __init__(self):
        self.maze = Maze()
        self.player = Player(self)

        self.width = 15
        self.length = 15

    def run_game(self):
        self.maze.create_maze(self.width, self.length)
        self.maze.define_item_square(self.length)

        running = True

        while running:
            map_printed = ''
            self.maze.create_maze_map(map_printed, self.width, self.length)

            bool_direction = False
            while not bool_direction:
                direction = input(
                    'Where do you want to go ? (Q,Z,D,S)')
                if direction == 'Q' and self.player.can_move_left():
                    self.player.move_left()
                    bool_direction = True
                elif direction == 'D' and self.player.can_move_right():
                    self.player.move_right()
                    bool_direction = True
                elif direction == 'Z' and self.player.can_move_up():
                    self.player.move_up()
                    bool_direction = True
                elif direction == 'S' and self.player.can_move_down():
                    self.player.move_down()
                    bool_direction = True

            self.player.take_item()
            running = self.player.is_victorious()

""" Import the time 
Import the module 'pygame' for writing video games
Import the other classes 'Maze' and 'Player' to manage the all game
Import the file 'config' for the constants.
"""
import time

import pygame

from mcgyver.maze import Maze
from mcgyver.player import Player
import config


class Game:

    """class that initiates the game of the maze, updates it according to each 
    action of the player and graphically displays the game.
    """

    def __init__(self):
        """function that instantiates the class "Game" by loading and resizing the 
        images of the game, defines the width and height of the maze and initializes 
        the grid and the player.
        """

        self.maze = Maze()
        self.player = Player(self)

        self.width = config.GAME_WIDTH
        self.length = config.GAME_HEIGHT
        self.dimension = config.GAME_SQUARE_DIMENSION

        self.wall_image = pygame.image.load(
            'mcgyver/assets/background/wall.png')
        self.wall_image = pygame.transform.scale(
            self.wall_image, (self.dimension, self.dimension))
        self.floor_image = pygame.image.load(
            'mcgyver/assets/background/floor.png')
        self.floor_image = pygame.transform.scale(
            self.floor_image, (self.dimension, self.dimension))
        self.player_image = pygame.image.load(
            'mcgyver/assets/characters/mac_gyver.png')
        self.player_image = pygame.transform.scale(
            self.player_image, (self.dimension-3, self.dimension-3))
        self.end_image = pygame.image.load(
            'mcgyver/assets/background/end.png')
        self.end_image = pygame.transform.scale(
            self.end_image, (self.dimension, self.dimension))
        self.guardian_image = pygame.image.load(
            'mcgyver/assets/characters/guardian.png')
        self.guardian_image = pygame.transform.scale(
            self.guardian_image, (self.dimension-2, self.dimension-2))
        self.ether_image = pygame.image.load('mcgyver/assets/items/ether.png')
        self.needle_image = pygame.image.load(
            'mcgyver/assets/items/needle.png')
        self.plastic_tube_image = pygame.image.load(
            'mcgyver/assets/items/plastic_tube.png')
        self.syringe_image = pygame.image.load(
            'mcgyver/assets/items/syringe.png')
        self.win = pygame.image.load(
            'mcgyver/assets/finish_game/win.png')
        self.win = pygame.transform.scale(self.win, (200, 200))
        self.defeat = pygame.image.load(
            'mcgyver/assets/finish_game/defeat.png')
        self.defeat = pygame.transform.scale(self.defeat, (200, 200))

    def run_game(self):
        """function that launches the game window and follows the player’s actions."""

        pygame.init()

        # define the dimensions of the game window
        number_squares = self.width
        size_squares = self.dimension
        screen_size = (number_squares * size_squares,
                       number_squares * size_squares)

        # generate the game window
        screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('Escape from the maze')

        pygame.font.init()
        myfont = pygame.font.Font(None, 24)

        self.maze.create_maze(self.width, self.length)
        self.maze.define_item_square(self.length)

        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.player.can_move_right():
                        self.player.move_right()
                    elif event.key == pygame.K_LEFT and self.player.can_move_left():
                        self.player.move_left()
                    elif event.key == pygame.K_UP and self.player.can_move_up():
                        self.player.move_up()
                    elif event.key == pygame.K_DOWN and self.player.can_move_down():
                        self.player.move_down()

            self.player.take_item()
            text_items_taken = (
                'You have taken {}/4 items'.format(self.player.number_items_taken))
            text = myfont.render(text_items_taken, 1, (255, 255, 255))
            self.__update_map(screen, text)

            running = self.player.is_victorious()[0]
            if not running:
                time.sleep(3)

    def __update_map(self, screen, text):
        """function that graphically displays the elements of the maze and that updates 
        it with each action of the player.
        """

        map_printed = ''
        map_in_window = self.maze.create_maze_map(
            map_printed, self.width, self.length)
        map_in_window = map_in_window.split(' ')

        index = 0
        for line_maze in range(self.width):
            for column_maze in range(self.length):
                if (line_maze, column_maze) != (0, 0):
                    index += 1
                if map_in_window[index] == '#':
                    screen.blit(self.wall_image,
                                (column_maze * self.dimension, line_maze * self.dimension))
                elif map_in_window[index] == 'x':
                    screen.blit(self.floor_image,
                                (column_maze * self.dimension, line_maze * self.dimension))
                    screen.blit(self.player_image,
                                (column_maze * self.dimension, line_maze * self.dimension))
                elif map_in_window[index] == 'a':
                    screen.blit(self.end_image,
                                (column_maze * self.dimension, line_maze * self.dimension))
                    screen.blit(self.guardian_image,
                                (column_maze * self.dimension, line_maze * self.dimension))
                else:
                    screen.blit(self.floor_image,
                                (column_maze * self.dimension, line_maze * self.dimension))
                    if map_in_window[index] == 'e':
                        screen.blit(self.ether_image,
                                    (column_maze * self.dimension, line_maze * self.dimension))
                    elif map_in_window[index] == 'n':
                        screen.blit(self.needle_image,
                                    (column_maze * self.dimension, line_maze * self.dimension))
                    elif map_in_window[index] == 'p':
                        screen.blit(self.plastic_tube_image,
                                    (column_maze * self.dimension, line_maze * self.dimension))
                    elif map_in_window[index] == 's':
                        screen.blit(self.syringe_image,
                                    (column_maze * self.dimension, line_maze * self.dimension))
                screen.blit(text, (20, 10))
                if self.player.is_victorious()[1] == 1:
                    screen.blit(self.win, ((self.width * self.dimension) /
                                           3, (self.length * self.dimension)/3))
                elif self.player.is_victorious()[1] == 0:
                    screen.blit(self.defeat, ((self.width * self.dimension) /
                                              3, (self.length * self.dimension)/3))

        pygame.display.flip()

        """ # for console game
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
            """

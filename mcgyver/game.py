import pygame
from maze import Maze
from player import Player

'''class that initiates the game of the maze, updates it according to each 
action of the player and graphically displays the game'''


class Game:

    '''function that instantiates the class "Game" by loading and resizing the 
    images of the game, defines the width and height of the maze and initializes 
    the grid and the player'''

    def __init__(self):
        self.maze = Maze()
        self.player = Player(self)

        self.width = 15
        self.length = 15

        self.wall_image = pygame.image.load(
            'mcgyver/assets/background/wall.png')
        self.wall_image = pygame.transform.scale(self.wall_image, (40, 40))
        self.floor_image = pygame.image.load(
            'mcgyver/assets/background/floor.png')
        self.floor_image = pygame.transform.scale(self.floor_image, (40, 40))
        self.player_image = pygame.image.load(
            'mcgyver/assets/characters/mac_gyver.png')
        self.player_image = pygame.transform.scale(self.player_image, (37, 37))
        self.end_image = pygame.image.load(
            'mcgyver/assets/background/end.png')
        self.end_image = pygame.transform.scale(self.end_image, (40, 40))
        self.guardian_image = pygame.image.load(
            'mcgyver/assets/characters/guardian.png')
        self.guardian_image = pygame.transform.scale(
            self.guardian_image, (38, 38))
        self.ether_image = pygame.image.load('mcgyver/assets/items/ether.png')
        self.needle_image = pygame.image.load(
            'mcgyver/assets/items/needle.png')
        self.plastic_tube_image = pygame.image.load(
            'mcgyver/assets/items/plastic_tube.png')
        self.syringe_image = pygame.image.load(
            'mcgyver/assets/items/syringe.png')

    '''function that launches the game window and follows the player’s actions'''

    def run_game(self):

        pygame.init()

        # define the dimensions of the game window
        number_squares = 15
        size_squares = 40
        screen_size = (number_squares * size_squares,
                       number_squares * size_squares)

        # generate the game window
        screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('Escape from the maze')

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
            self.__update_map(screen)
            running = self.player.is_victorious()

    '''function that graphically displays the elements of the maze and that updates 
    it with each action of the player'''

    def __update_map(self, screen):
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
                                (column_maze * 40, line_maze * 40))
                elif map_in_window[index] == 'f':
                    screen.blit(self.floor_image,
                                (column_maze * 40, line_maze * 40))
                elif map_in_window[index] == 'x':
                    screen.blit(self.floor_image,
                                (column_maze * 40, line_maze * 40))
                    screen.blit(self.player_image,
                                (column_maze * 40, line_maze * 40))
                elif map_in_window[index] == 'a':
                    screen.blit(self.end_image,
                                (column_maze * 40, line_maze * 40))
                    screen.blit(self.guardian_image,
                                (column_maze * 40, line_maze * 40))
                else:
                    screen.blit(self.floor_image,
                                (column_maze * 40, line_maze * 40))
                    if map_in_window[index] == 'e':
                        screen.blit(self.ether_image,
                                    (column_maze * 40, line_maze * 40))
                    elif map_in_window[index] == 'n':
                        screen.blit(self.needle_image,
                                    (column_maze * 40, line_maze * 40))
                    elif map_in_window[index] == 'p':
                        screen.blit(self.plastic_tube_image,
                                    (column_maze * 40, line_maze * 40))
                    elif map_in_window[index] == 's':
                        screen.blit(self.syringe_image,
                                    (column_maze * 40, line_maze * 40))

        pygame.display.flip()

        ''' # for console game
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
            '''

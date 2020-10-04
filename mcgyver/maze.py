import random

'''class that manages the different elements that make up the maze'''


class Maze:

    '''function that instantiates the lists or tuples of the postions of the various elements of the maze'''

    def __init__(self):
        self.wall = []
        self.floor = []
        self.start = (0, 0)
        self.end = (0, 0)
        self.items_position = {}
        self.player_position = (0, 0)
        self.guardian = (0, 0)

    '''function that read the maze file and convert each part of the maze (wall, floor, ...) in geographic coordinates
    and put them in their respective lists or tuples'''

    def create_maze(self, width, length):

        maze = []
        index = 0

        for line_maze in range(length):
            maze.append([0] * width)

        maze_file = open("mcgyver/maze_grid.txt", "r")
        contenu_maze_file = maze_file.read()
        contenu_maze_file = contenu_maze_file.split()

        for column_maze in range(width):
            for line_maze in range(length):
                if (column_maze, line_maze) != (0, 0):
                    index += 1
                maze[column_maze][line_maze] = contenu_maze_file[index]

        maze_file.close()

        for line_maze in range(width):
            for column_maze in range(length):
                if maze[line_maze][column_maze] == '9':
                    self.wall.append((column_maze, line_maze))
                if maze[line_maze][column_maze] == '0':
                    self.floor.append((column_maze, line_maze))
                if maze[line_maze][column_maze] == '1':
                    self.start = (column_maze, line_maze)
                    self.floor.append((column_maze, line_maze))
                if maze[line_maze][column_maze] == '2':
                    self.end = (column_maze, line_maze)
                self.player_position = self.start
                self.guardian = self.end

    '''function that initializes the random position of items in the maze as 
    coordinates stored in a list of items'''

    def define_item_square(self, length):
        nb_items = 0
        while nb_items != 4:
            if nb_items == 0:
                name = 'e'
            elif nb_items == 1:
                name = 'n'
            elif nb_items == 2:
                name = 'p'
            elif nb_items == 3:
                name = 's'

            position = False
            while position == False:
                item_provisory_position = (random.randint(
                    1, length), random.randint(1, length))
                index = 0
                for floor in self.floor:
                    if item_provisory_position == floor:
                        position = True
                        self.items_position[name] = item_provisory_position
                        break
                    else:
                        position = False
                    index += 1
            nb_items += 1

    '''function that creates the maze as a text and returns it'''

    def create_maze_map(self, map_printed, width, length):
        position_map = (0, 0)
        item_placement = False
        player_placement = False

        for line_maze in range(width):
            for column_maze in range(length):
                position_map = (column_maze, line_maze)
                for wall in self.wall:
                    if position_map == wall:
                        map_printed += '# '
                if position_map == self.player_position:
                    map_printed += 'x '
                    player_placement = True
                for key, value in self.items_position.items():
                    if position_map == value:
                        map_printed += key + ' '
                        item_placement = True
                if not item_placement and not player_placement:
                    for floor in self.floor:
                        if position_map == floor:
                            map_printed += 'f '
                if position_map == self.end:
                    map_printed += 'a '
                item_placement = False
                player_placement = False

        # print(map_printed) ## for console game
        return map_printed

    '''function that checks that the next location wanted by the player is a floor'''

    def next_square_is_floor(self, add_x, add_y):
        next_player_square = (
            self.player_position[0] + add_x, self.player_position[1] + add_y)
        for floor_square in self.floor:
            if next_player_square == floor_square:
                return True
        for item_square in self.items_position:
            if next_player_square == item_square:
                return True

    '''function that checks that the location on which the player is located is occupied by an item'''

    def square_is_item(self):
        for key, value in self.items_position.items():
            if self.player_position == value:
                return True

    '''function that checks that the player’s right square is the finish square'''

    def next_square_is_arrival(self):
        next_player_square = (
            self.player_position[0] + 1, self.player_position[1])
        if next_player_square == self.end:
            return True

    '''function that deletes an item when the player is on the same square as the item'''

    def remove_item(self):
        position_removed_item = self.player_position
        for key, value in self.items_position.items():
            if position_removed_item == value:
                break
        del(self.items_position[key])

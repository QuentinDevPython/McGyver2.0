'''class that manages the player’s actions'''


class Player:

    '''function that recovers the state of the game'''

    def __init__(self, game):
        self.game = game

    '''function that checks that the player can move to the right'''

    def can_move_right(self):
        if self.game.maze.next_square_is_floor(1, 0):
            return True

    '''function that will change the position of the player to move to the right'''

    def move_right(self):
        self.game.maze.player_position = (
            self.game.maze.player_position[0] + 1,
            self.game.maze.player_position[1]
        )

    '''function that checks that the player can move to the left'''

    def can_move_left(self):
        if self.game.maze.next_square_is_floor(-1, 0):
            return True

    '''function that will change the position of the player to move to the left'''

    def move_left(self):
        self.game.maze.player_position = (
            self.game.maze.player_position[0] - 1,
            self.game.maze.player_position[1]
        )

    '''function that checks that the player can move up'''

    def can_move_up(self):
        if self.game.maze.next_square_is_floor(0, -1):
            return True

    '''function that will change the position of the player to move up'''

    def move_up(self):
        self.game.maze.player_position = (
            self.game.maze.player_position[0],
            self.game.maze.player_position[1] - 1
        )

    '''function that checks that the player can move down'''

    def can_move_down(self):
        if self.game.maze.next_square_is_floor(0, 1):
            return True

    '''function that will change the position of the player to move down'''

    def move_down(self):
        self.game.maze.player_position = (
            self.game.maze.player_position[0],
            self.game.maze.player_position[1] + 1
        )

    '''function that allows the player to retrieve an item and thus remove the item from the maze'''

    def take_item(self):
        if self.game.maze.square_is_item():
            self.game.maze.remove_item()

    '''function that verifies that the player has retrieved the items when he comes in front 
    of the finish box. It displays whether the player has won or not'''

    def is_victorious(self):
        running = True
        if self.game.maze.next_square_is_arrival():
            if self.game.maze.items_position == {}:
                print('Win')
                running = False
            else:
                print('Defeat')
                running = False
        return running

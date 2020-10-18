class Player:
    """class that manages the player’s actions."""

    def __init__(self, game):
        """function that recovers the state of the game."""

        self.game = game
        self.number_items_taken = 0

    def can_move_right(self):
        """function that checks that the player can move to the right."""

        if self.game.maze.next_square_is_floor(1, 0):
            return True

    def move_right(self):
        """function that will change the position of the player to move to the right."""

        self.game.maze.player_position = (
            self.game.maze.player_position[0] + 1,
            self.game.maze.player_position[1]
        )

    def can_move_left(self):
        """function that checks that the player can move to the left."""

        if self.game.maze.next_square_is_floor(-1, 0):
            return True

    def move_left(self):
        """function that will change the position of the player to move to the left."""

        self.game.maze.player_position = (
            self.game.maze.player_position[0] - 1,
            self.game.maze.player_position[1]
        )

    def can_move_up(self):
        """function that checks that the player can move up."""

        if self.game.maze.next_square_is_floor(0, -1):
            return True

    def move_up(self):
        """function that will change the position of the player to move up."""

        self.game.maze.player_position = (
            self.game.maze.player_position[0],
            self.game.maze.player_position[1] - 1
        )

    def can_move_down(self):
        """function that checks that the player can move down."""

        if self.game.maze.next_square_is_floor(0, 1):
            return True

    def move_down(self):
        """function that will change the position of the player to move down."""

        self.game.maze.player_position = (
            self.game.maze.player_position[0],
            self.game.maze.player_position[1] + 1
        )

    def take_item(self):
        """function that allows the player to retrieve an item and thus remove the item from the maze."""

        if self.game.maze.square_is_item():
            self.number_items_taken += 1
            self.game.maze.remove_item()

    def is_victorious(self):
        """function that verifies that the player has retrieved the items when he comes in front 
        of the finish box. It displays whether the player has won or not.
        """

        running = True
        state_victory = 2
        if self.game.maze.next_square_is_arrival():
            if self.game.maze.items_position == {}:
                state_victory = 1
                running = False
            else:
                running = False
                state_victory = 0
        return running, state_victory

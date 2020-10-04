class Player:

    def __init__(self, game):
        self.game = game

    def can_move_right(self):
        if self.game.maze.next_square_is_floor(1, 0):
            return True

    def move_right(self):
        self.game.maze.player_position = (
            self.game.maze.player_position[0] + 1,
            self.game.maze.player_position[1]
        )

    def can_move_left(self):
        if self.game.maze.next_square_is_floor(-1, 0):
            return True

    def move_left(self):
        self.game.maze.player_position = (
            self.game.maze.player_position[0] - 1,
            self.game.maze.player_position[1]
        )

    def can_move_up(self):
        if self.game.maze.next_square_is_floor(0, -1):
            return True

    def move_up(self):
        self.game.maze.player_position = (
            self.game.maze.player_position[0],
            self.game.maze.player_position[1] - 1
        )

    def can_move_down(self):
        if self.game.maze.next_square_is_floor(0, 1):
            return True

    def move_down(self):
        self.game.maze.player_position = (
            self.game.maze.player_position[0],
            self.game.maze.player_position[1] + 1
        )

    def take_item(self):
        if self.game.maze.square_is_item():
            self.game.maze.remove_item()

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

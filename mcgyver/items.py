class Items():

    def __init__(self, image_name, game):
        self.player = Player(game)
        self.rect = self.image.get_rect()
        self.item_position = self.position
        self.rect.x = self.item_position[0]
        self.rect.y = self.item_position[1]

    def remove(self):
        self.player.game.all_items.remove(self)

    @property
    def position(self):
        item_position = self.player.maze.is_item_square

        item_position = (
            item_position[0] * 40, item_position[1] * 40)

        return item_position

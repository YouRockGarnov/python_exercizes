

class Player:
    def __init__(self):
        self.cur_start = "start"
        self.cur_ready = "ready"

    def __getattribute__(self, name):
        if name == object.__getattribute__(self, "cur_ready"):
            return object.__getattribute__(self, "update")

        else:
            result = object.__getattribute__(self, name)
            return result

    def update(self, start, ready):
        self.cur_start = start
        self.cur_ready = ready


def play(game_obj):
    player = Player()

    while True:
        getattr(game_obj, player.cur_start)(player)

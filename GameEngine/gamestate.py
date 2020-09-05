class GameState:

    def __init__(self):
        self.game_state_manager = None
        self.ui_element_manager = None

    def start(self):
        pass

    def update(self):
        pass

    def exit(self):
        del self.game_state_manager
        del self.ui_element_manager

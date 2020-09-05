from GameEngine import *
from game import Game


class MainMenu(GameState):

    def __init__(self, screen):
        GameState.__init__(self)

        self.screen = screen
        self.label = None
        self.button = None

    def start(self):
        self.button = Button(text='Start Game', background=(255, 255, 255),
                             command=self.start_game, position=(300, 250))
        self.label = Label('Pillar Run', (255, 255, 255), position=(300, 100))
        self.ui_element_manager.add(self.label)
        self.ui_element_manager.add(self.button)

    def start_game(self):
        self.game_state_manager.change_state(Game(self.screen))

from GameEngine import UIElement
import pygame


class Label(UIElement):

    def __init__(self, text=None, color=(0, 0, 0), background=None, font=None, position=(0, 0)):
        UIElement.__init__(self)
        self.text = text
        self.color = color
        self.background = background
        self.position = position

        if font:
            self.font = font
        else:
            self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], 16, bold=True)

        if text:
            self.image = self.font.render(self.text, True, self.color, self.background)
            self.rect = self.image.get_rect()
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]

    def set_label(self, text, color=None, background=None, font=None, position=None):
        self.text = text

        if position:
            self.position = position

        if font:
            self.font = font

        if color:
            self.color = color

        if background:
            self.background = background

        self.image = self.font.render(self.text, True, self.color, self.background)
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

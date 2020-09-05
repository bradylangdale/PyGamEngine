from GameEngine import UIElement
import pygame


class Button(UIElement):

    def __init__(self, image=None, image_path=None, text=None, color=(0, 0, 0), background=None,
                 font=None, position=(0, 0), command=None):
        UIElement.__init__(self)
        self.text = text
        self.color = color
        self.background = background
        self.position = position
        self.command = command

        if image:
            self.image = image
            self.rect = image.get_rect()
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]

        if font:
            self.font = font
        else:
            self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], 16, bold=True)

        if text:
            self.image = self.font.render(self.text, True, self.color, self.background)
            self.rect = self.image.get_rect()
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        elif image_path:
            self.image = pygame.image.load(image_path)
            self.rect = self.image.get_rect()
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]

    def set_button(self, image=None, image_path=None, command=None, text=None,
                   color=None, background=None, font=None, position=None):
        if position:
            self.position = position

        if command:
            self.command = command

        if image:
            self.image = image
            self.rect = image.get_rect()
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]

        if image_path:
            self.image = pygame.image.load(image_path)
            self.rect = image.get_rect()
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]

        if text or font:
            if text:
                self.text = text

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

    def mouse_up(self, button):
        if button == 1:
            if self.command:
                self.command()


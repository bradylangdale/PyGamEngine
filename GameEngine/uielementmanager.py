import pygame


class UIElementManager:

    def __init__(self, surface):
        self.surface = surface
        self.elements = []
        self.button_up = 0
        self.button_down = 0

    def update(self):
        for element in self.elements:
            if element.visible:
                element.update()
                self.surface.blit(element.image, element.rect)

                if element.rect.collidepoint(pygame.mouse.get_pos()):
                    if not element.hover:
                        element.hover = True
                        element.hover_begin()
                    if self.button_up != 0:
                        element.mouse_up(self.button_up)
                    if self.button_down != 0:
                        element.mouse_down(self.button_down)
                elif element.hover:
                    element.hover_end()
                    element.hover = False

    def add(self, element):
        element.ui_element_manager = self
        self.elements.append(element)


class UIElement:

    def __init__(self):
        self.image = None
        self.rect = None
        self.visible = True
        self.ui_element_manager = None
        self.hover = False

    def update(self):
        pass

    def hover_begin(self):
        pass

    def hover_end(self):
        pass

    def mouse_down(self, button):
        pass

    def mouse_up(self, button):
        pass

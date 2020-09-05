class GameObject:

    def __init__(self):
        self.image = None
        self.rect = None
        self.physics = False
        self.dynamic = False
        self.rotates = True
        self.body = None
        self.active = True
        self.density = 1

    def update(self):
        pass

    def collision_begin(self, game_object):
        pass

    def collision_end(self, game_object):
        pass

    def pre_collision_solve(self, game_object, old_manifold):
        pass

    def post_collision_solve(self, game_object, impulse):
        pass

from Box2D import *
from GameEngine import ContactHandler
import math


class GameObjectHandler:

    def __init__(self, game_objects=None, b2_scale=32):
        if game_objects is None:
            game_objects = []
        self.world = Box2D.b2World()  # create instance of box 2d world
        self.b2_scale = b2_scale  # scaling parameter, is equal to pixels to meter
        self.game_objects = []  # game object list
        self.contact_handler = ContactHandler()
        self.world.contactListener = self.contact_handler

        if game_objects:  # checks to see if there are objects in list
            for game_object in game_objects:  # iterates through list
                self.add(game_object)  # if so calls add function

    def set_b2_scale(self, scale):
        self.b2_scale = scale

    def update(self):
        self.world.Step(1 / 60, 6, 2)
        self.world.ClearForces()

        for game_obj in self.game_objects:
            if game_obj.physics:
                game_obj.rect.x = game_obj.body.position.x * self.b2_scale - game_obj.rect.width / 2
                game_obj.rect.y = -game_obj.body.position.y * self.b2_scale - game_obj.rect.height / 2
            if game_obj.active:
                game_obj.update()

    def get_images(self):
        images = []
        for game_object in self.game_objects:
            images.append(game_object.image)
        return images

    def get_rects(self):
        rects = []
        for game_object in self.game_objects:
            rects.append(game_object.rect)
        return rects

    def get_angles(self):
        angles = []
        for game_object in self.game_objects:
            angles.append(math.degrees(game_object.body.angle))
        return angles

    def get_game_object_of_type(self, type_of):
        for game_object in self.game_objects:
            if isinstance(game_object, type_of):
                return game_object

    def get_game_objects_of_type(self, type_of):
        game_objects = []
        for game_object in self.game_objects:
            if isinstance(game_object, type_of):
                game_objects.append(game_object)
        return game_objects

    def add(self, game_object):
        self.game_objects.append(game_object)  # adds game object to list of game objects

        if game_object.physics:  # checks if game objects have physics attributes
            body = self.world.CreateBody(  # if so then, the code will create rigid body for game objects
                position=(game_object.rect.x / self.b2_scale, -game_object.rect.y / self.b2_scale),
                type=Box2D.b2_dynamicBody if game_object.dynamic else Box2D.b2_staticBody,
                userData=game_object,  # create references for each other
                fixedRotation=game_object.rotates)
            body.CreatePolygonFixture(
                box=(game_object.rect.width / 2 / self.b2_scale, game_object.rect.height / 2 / self.b2_scale),
                density=game_object.density,
                friction=0.5)
            game_object.body = body

    def exit(self):
        del self.game_objects
        del self.world
        del self.contact_handler
        del self.b2_scale


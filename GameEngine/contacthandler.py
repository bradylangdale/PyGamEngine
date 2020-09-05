from Box2D import *


class ContactHandler(b2ContactListener):
    """
    directs collisions in box2d to game objects

    """

    def __init__(self):
        b2ContactListener.__init__(self)

    def BeginContact(self, contact):
        body_a = contact.fixtureA.body.userData
        body_b = contact.fixtureB.body.userData
        body_a.collision_begin(body_b)
        body_b.collision_begin(body_a)

    def EndContact(self, contact):
        body_a = contact.fixtureA.body.userData
        body_b = contact.fixtureB.body.userData
        body_a.collision_end(body_b)
        body_b.collision_end(body_a)

    def PreSolve(self, contact, old_manifold):
        body_a = contact.fixtureA.body.userData
        body_b = contact.fixtureB.body.userData
        body_a.pre_collision_solve(body_b, old_manifold)
        body_b.pre_collision_solve(body_a, old_manifold)

    def PostSolve(self, contact, impulse):
        body_a = contact.fixtureA.body.userData
        body_b = contact.fixtureB.body.userData
        body_a.post_collision_solve(body_b, impulse)
        body_b.post_collision_solve(body_a, impulse)

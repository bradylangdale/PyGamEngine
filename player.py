import pygame.key as pgk
import pygame.locals as pl
from GameEngine import *


class Player(GameObject):
	"""The player class that is going to be used inside the game"""

	def __init__(self, x, y, image):
		"""Creates a player.
		Parameters:
			x (int): The starting x of the player
			y (int): The starting y of the player
			image (string): Player image
		Return Value: None"""
		# Call the parent class (Sprite) constructor
		GameObject.__init__(self)

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = image

		# Fetch the rectangle object that has the dimensions of the image
		# Set an initial position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.max_run_speed = 5
		self.run_force = 1

		# Jumping variables
		self.max_jump_speed = 6
		self.jump_force = 3.5  # Change this for the player to be able to jump higher
		self.jumping = False
		self.hp = 100

		# Physics variables
		self.physics = True
		self.dynamic = True
		self.touches_above = 0
		self.touches_below = 0
		self.touches_left = 0
		self.touches_right = 0

		self.dead = False

	@property
	def can_move(self):
		"""Determines whether the player can move
		Return value:
			True if can, False if not"""
		return self.can_move_left or self.can_move_right

	@property
	def can_move_right(self):
		"""Determines whether the player can move right
		Return value:
			True if can, False if not"""
		return not self.touching_right

	@property
	def can_move_left(self):
		"""Determines whether the player can move left
		Return value:
			True if can, False if not"""
		return not self.touching_left

	@property
	def can_jump(self):
		"""Determines whether a player can jump.
		Return Value:
			True on success, False on failure"""
		return self.touching_below and not self.touching_above

	@property
	def is_jumping(self):
		"""Determines whether the player is jumping"""
		return self.jumping

	@property
	def is_falling(self):
		"""Determines whether the player is falling
		Return Value:
			True on success, False on failure"""
		return not self.touching_below and not self.touching_above

	@property
	def touching_above(self):
		return True if self.touches_above > 0 else False

	@property
	def touching_below(self):
		return True if self.touches_below > 0 else False

	@property
	def touching_left(self):
		return True if self.touches_left > 0 else False

	@property
	def touching_right(self):
		return True if self.touches_right > 0 else False

	def move(self):
		"""Moves the player.
		Return Value:
			None"""
		keys = pgk.get_pressed()
		# Applies force to the players physical body
		self.jumping = False
		dx, dy = 0, 0
		if keys[pl.K_UP] == 1 and self.can_jump and self.body.linearVelocity.y < self.max_jump_speed:
			dy += 1
			self.jumping = True
		if keys[pl.K_RIGHT] == 1 and self.body.linearVelocity.x < self.max_run_speed:
			dx += 1
		elif keys[pl.K_LEFT] == 1 and self.body.linearVelocity.x > -self.max_run_speed:
			dx -= 1

		self.body.ApplyLinearImpulse(
			impulse=(dx * self.body.mass * self.run_force, dy * self.body.mass * self.jump_force),
			point=(self.body.position.x, self.body.position.y),
			wake=True)

		if dx != 0 or dy != 0:
			print(self.rect.x, self.rect.y)

	def update(self):
		"""Calls the player internal functions
			Return Value: None"""
		self.move()

		# reset touch count these are counters that are incremented during physics calculations
		self.touches_above = 0
		self.touches_below = 0
		self.touches_left = 0
		self.touches_right = 0

	def collision_begin(self, game_object):
		if game_object.image.get_at((0, 0)) == (237, 28, 36, 255):
			self.dead = True

	def post_collision_solve(self, game_object, impulse):
		# increment touch counters
		self.touches_below += self.is_object_below(game_object.rect)
		self.touches_above += self.is_object_above(game_object.rect)
		self.touches_left += self.is_object_left(game_object.rect)
		self.touches_right += self.is_object_right(game_object.rect)

	def hit(self, value):
		"""Hits, or heals, the player, depending on the value Parameters: value (int): How much damage we should hit
		the player for, can be positive or negative, negative will hurt and positive will heal Return Value: None """
		self.hp += value

	def is_object_below(self, rect):
		if self.rect.bottom <= rect.top:
			return 1
		else:
			return 0

	def is_object_above(self, rect):
		if self.rect.top >= rect.bottom:
			return 1
		else:
			return 0

	def is_object_left(self, rect):
		if self.rect.left >= rect.right:
			return 1
		else:
			return 0

	def is_object_right(self, rect):
		if self.rect.right <= rect.left:
			return 1
		else:
			return 0

import pygame as pg
from vector import Vector
from timer import Timer
from pygame.sprite import Sprite, Group
#from sound import Sound
from spritesheet import Spritesheet

class Mario(Sprite):

    #x,y,x+offset,y+offset


    #exploding_images = [pg.image.load(f'images/explode{n}.png') for n in range(8)]
    #images = [pg.image.load(f'images/ship.bmp') for n in range(1)]


    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.display = game.display
        self.level = game.level
    #    self.sound = game.sound
    #    self.alien_fleet = None
    #    self.lasers = None
        self.stats = game.stats
        #self.image = pg.image.load('images/ship.bmp')

        filename = 'images/allsprites.png'
        allSprites = Spritesheet(filename)
        mario_rect = (70, 0, 32, 32)
        self.mario_image = allSprites.image_at(mario_rect)

        #mario_images = pg.image.load(mario_image)
        self.rect = self.mario_image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.center_bottom()
        self.v = Vector()
    #    self.firing = False
        self.frames = 0
        #self.exploding_timer = Timer(image_list=Ship.exploding_images, delay=200, is_loop=False)
        #self.normal_timer = Timer(image_list=self.mario_image, delay=1000, is_loop=True)
    #    self.timer = self.normal_timer
    #    self.dying = False

    #def set_alien_fleet(self, alien_fleet):
    #    self.alien_fleet = alien_fleet

    #def set_lasers(self, lasers):
    #    self.lasers = lasers

    def center_bottom(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = Vector(self.rect.centerx, self.rect.centery)

   # def reset_timer(self):
        #self.exploding_timer.reset()
        #self.normal_timer.reset()
        #self.timer = self.normal_timer

    #def toggle_firing(self):
   #     self.firing = not self.firing

    #def hit(self):
   #     self.timer = self.exploding_timer
    #    self.dying = True
    #    self.sound.play_ship_explosion()

    #def is_dying(self):
    #    return self.dying

   # def die(self):
    #    self.stats.ship_hit()
    #    if self.stats.ships_left == 0:
    #        self.game.finished = True
    #    self.dying = False
    #    self.game.restart()

    def moving(self, vector):
        self.v = vector

    def inc_add(self, other):
        self.v += other

    def clamp(self):
        rw, rh = self.rect.width, self.rect.height
        srw, srb = self.screen_rect.width, self.screen_rect.bottom
        x, y = self.center.x, self.center.y

        self.center.x = min(max(x, rw / 2), srw - rw / 2)
        self.center.y = min(max(y, rh / 2), srb - rh / 2)

    def update(self):
    #    if self.dying and self.timer.is_expired():
    #        self.die()
        self.center += self.v * self.settings.ship_speed_factor

        self.clamp()
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y
    #    if self.frames % 10 == 0 and self.firing:
    #        self.lasers.fire()
        self.frames += 1

        if self.rect.centerx > self.settings.screen_width / 2 + 1:
            self.center.x = self.settings.screen_width / 2
        if self.rect.centerx >= self.settings.screen_width/2:
            if self.v.x > 0:
                self.stats.moveFoward = self.v.x * self.settings.ship_speed_factor
            else:
                self.stats.moveFoward = 0
        else:
            self.stats.moveFoward = 0
        #print(self.stats.moveFoward)
        #self.display.move(self.v * self.settings.ship_speed_factor, 0)

    def draw(self):
        #image = self.timer.image()
        rect = self.mario_image.get_rect()
        rect.x, rect.y = self.rect.x, self.rect.y
        self.screen.blit(self.mario_image, rect)
        # self.screen.blit(self.image, self.rect)
        # pg.draw.rect(self.screen, Game.RED, self.rect, 1)

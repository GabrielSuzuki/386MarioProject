import pygame as pg
#from landing_page import LandingPage
from sys import exit
import game_functions as gf
from time import sleep
from stats import Stats
#from scoreboard import Scoreboard
#from laser import Lasers
from mario import Mario
#from alien import AlienFleet
from settings import Settings
#from sound import Sound
#from barrier import Barriers
from random import randint
from level import Level
from display import Display
class Game:
    RED = (255, 0, 0)
    pg

    def __init__(self):
        pg.init()
        #self.background = pg.image.load(f'images/NES - Super Mario Bros - World 1-1.png')
        self.settings = Settings()
        self.stats = Stats(game=self)
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        #self.sound = Sound()
        #self.sb = Scoreboard(game=self)
        pg.display.set_caption("Mario Game")
        self.lvl_map = None
        self.level = Level(self.screen, self.settings)
        self.display = Display(self.screen, self.stats, game=self)
        self.mario = Mario(game=self)
        #self.ship = Ship(game=self)
        #self.alien_fleet = AlienFleet(game=self)
        #self.lasers = Lasers(game=self, owner=self.ship)                  # for ship lasers
        #self.alien_lasers = Lasers(game=self, owner=self.alien_fleet)   # for alien lasers
        #self.barrier = Barriers(game=self)
        #self.alien_fleet.set_lasers(self.alien_lasers)
        #self.ship.set_alien_fleet(self.alien_fleet)
        #self.ship.set_lasers(self.lasers)
        #self.shipCount = 0
        #self.bg1 = False
        #self.bg2 = False

        #unfinished
        #for pipe in pipes:
        #    secret_pipes.add(pipe)

        #flag = Flag(screen,settings,stats)
        #flags.add(flag)
        #pole = Pole(screen, settings)
        #poles.add(pole)

        # might need to add flag/pole

        #mario = Mario(screen,settings,pipes,bricks,upgrades,fireballs,secret_bricks,secret_pipes,goomba,koopa)

        #level = Level(screen,settings,pipes,lvl_map,bricks,pipes,secret_pipes,goomba,koopa)



        #clips[0].play[-1]
        #while True:
            #Checks if Mario in in the main level
            #does only once
            #if stats.activate_main_lvl:
                #might need to add flag/pole
            #    lvl_map = Map(screen, settings, bricks, pipes,secret_pipes, goombas, koopas)
            #    lvl_map.build_brick()
                #generate pipes and flag/pole
            #    for i in range(0,6):
            #        pipe = Pipe(screen,settings,i)
            #        pipes.add(pipe)
            #    flag = Flag(screen,settings,stats)
            #    flags.add(flag)
            #    pole = Pole(screen, settings)
            #    poles.add(pole)
            #   stats.activate_main_lvl = False
            #Checks if Mario has activated the secret level
            #does this only once
            #if stats.activate_secret:
                #clears everything belonging to main level to
            #    pipes.empty()
            #    bricks.empty()
            #    enemies.empty()
            #    poles.empty()
            #    flags.empty()
            #    lvl_map = Map(screen,settings,bricks,pipes,mario,poles,flags,enemies)
            #    lvl_map.build_brick()

            #    stats.activate_secret = False
            #    stats.main_level = False




    def restart(self):
        #if self.stats.ships_left == 0:
        #  self.game_over()
        print("restarting game")
        while self.sound.busy():    # wait for explosion sound to finish
            pass
        #self.lasers.empty()
        #self.alien_fleet.empty()
        #self.alien_fleet.create_fleet()
        self.mario.center_bottom()
        #self.ship.center_bottom()
        #self.ship.reset_timer()
        self.update()
        self.draw()
        #self.sound.stop_bg()
        #self.bg1 = False
        #self.bg2 = False
        #self.sound.play_bg()
        sleep(0.5)

    def update(self):
        self.mario.update()
        self.display.move()
        #self.ship.update()
        #self.alien_fleet.update()
        #self.lasers.update()
        #self.alien_lasers.update()
        #self.sb.update()
        #self.barrier.update()
        #self.shipCount = 0
        #for i in self.alien_fleet.fleet:
        #    self.shipCount += 1
        #if self.shipCount > 10 and self.shipCount < 21 and self.bg1 == False:
        #    self.sound.stop_bg()
        #    self.bg1 = True
        #    self.sound.speed_up_bg1()
        #elif self.shipCount < 10 and self.bg2 == False:
        #    self.sound.stop_bg()
        #    self.bg2 = True
        #    self.sound.speed_up_bg2()
        self.temp = 1

    def draw(self):
        self.screen.fill(self.bg_color)
        self.level.blitme()
        self.mario.draw()
        #self.ship.draw()
        #self.alien_fleet.draw()
        #self.lasers.draw()
        #self.alien_lasers.draw()
        #self.sb.draw()
        #self.barrier.draw()
        pg.display.flip()

    def play(self):
        self.finished = False
        #print(self.shipCount)
        #self.sound.play_bg()

        while not self.finished:
            self.update()
            self.draw()
            gf.check_events(game=self)   # exits game if QUIT pressed
        self.game_over()

    def game_over(self):
    #  self.sound.play_game_over()
      print('\nGAME OVER!\n\n')
      exit()    # can ask to replay here instead of exiting the game

def main():
    g = Game()
    #lp = LandingPage(game=g)
    #lp.show()
    g.play()

    #unfinished
    #stats.game_active()
    #gf.check_events(mario, stats, clips, fireballs)
    #if mario.rect.right >= 600 and stats.main_level:
    #    diff = mario.rect.right - 600
    #    mario.rect.right = 600
    #    level.shifting_world(-diff)

    #if the play gets near the left side,shift the world right commented
    #if mario.rect.left <= 100
    #    diff = 100 - mario.rect.left
    #    mario.rect.left = 100
    #    level.shifting_world(diff)

    #gf.update_screen(screen,mario,settings,level,pipes,display,flags,poles,radio,clips,fireballs,secret_pipes)
    #pygame.display.flip()

if __name__ == '__main__':
    main()

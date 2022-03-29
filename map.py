from settings import Settings
from stats import Stats
class Map:
    BRICK_SIZE = 40

    def __init__(self,screen,bricks,pipes,mario,secret_bricks,upgrades,enemies,ground):
        self.screen = screen
        self.settings = Settings
        self.stats = Stats
        self.bricks = bricks
        self.secret_bricks = secret_bricks
        self.pipes = pipes
        self.mario = mario
        self.upgrades = upgrades
        self.enemies = enemies
        self.ground = ground
        self.main_level = "images/level_loc.txt"
        self.secret_level = "images/Underground_Level.txt"

    #need to finish stats
        #checks for main or secret level
        if not self.stats.activate_secret:
            with open(self.main_level, 'r') as f:
                self.rows = f.readlines()
                if self.stats.return_main_level:
                    #put mario at the pipe near the end
                    self.mario.rect.x = 7210
                    self.mario.rect.y = 500
        if self.stats.activate_secret:
            with open(self.secret_level, 'r') as f:
                self.rows = f.readlines()
                #has mario fall into secret level
                self.mario.rect.x = 100
                self.mario.rect.y = 100

        self.brick = None
        self.goomba = None
        self.koopa = None
        self.coin = None
        self.deltax = self.deltay = Map.BRICK_SIZE

    def build_brick(self):
        dx, dy = self.deltax,self.deltay
    #alot left to do
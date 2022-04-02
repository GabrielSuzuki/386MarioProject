from settings import Settings
from stats import Stats
class Map:
    #BRICK_SIZE = 40
    BRICK_SIZE = 32

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
        self.rows = None
        self.entityList = []

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


    def loadLevel(self):
        pass

    def loadEntities(self):
        rowCount = self.Settings.screen_height
        colCount = 0
        if not self.stats.activate_secret:
            for string in self.rows:
                rowCount -= self.deltay
                # x,y coords
                for element in string:
                    if element == '?':
                        # Item_Brick.png
                        self.addRandomBox(rowCount,colCount)
                    if element == 'G':
                        # in allsprites
                        self.addGoomba(rowCount,colCount)
                    if element == 'X':
                        # Ground_Brick.png
                        self.addGroundBrick(rowCount,colCount)
                    if element == 'R':
                        # Stair_Brick.png
                        self.addStair(rowCount,colCount)
                    if element == 'K':
                        # in all sprites
                        self.addKoopa(rowCount,colCount)
                    if element == 'C':
                        # Coin.png
                        self.addCoin(rowCount,colCount)
                    if element == 'M':
                        # Mushroom.png
                        self.addMushroom(rowCount,colCount)
                    if element == 'I':
                        # Invisible_Block.png -> 1UP_Mushroom.png
                        self.invisableBlock(rowCount,colCount)
                    if element == 'L':
                        # Red_Brick.png -> Empty_Brick.png
                        self.addMultiHitBlock(rowCount,colCount)
                    if element == 'S':
                        # Red_Brick.png -> Star.png
                        self.addStar(rowCount,colCount)
                    colCount += self.deltax

    def loadLayers(self):
        pass

    def loadObjects(self):
        pass

    def updateEntities(self):
        pass

    def drawLevel(self):
        pass

    def build_brick(self):
        dx, dy = self.deltax,self.deltay
    #alot left to do

    def addRedBrick(self,x,y):
        #Breakable, star?, invisible?
        pass

    def addStair(self,x,y):
        pass

    def addRandomBox(self,x,y,type):
        #type = type of block(upgrade, coin, invisible, star, breakable, invisible)
        self.entityList.append(Block(self.screen, x,y,self.type))
        #self.entityList.append(
        #    RandomBox(
        ##        self.screen,
         #       self.sprites.spriteCollection,
        #        x,
        #        y,
        #        self.sound,
        #        self.dashboard,
        #    )
        pass

    def addGoomba(self,x, y):
        self.entityList.append(
            Goomba(self.screen, self.sprites.spriteCollection, x, y, self)
        )
        pass

    def addKoopa(self,x ,y):
        self.entityList.append(
            Koopa(self.screen, self.sprites.spriteCollection, x, y, self)
        )
        pass

    def addCoin(self, x ,y):
        self.entityList.append(Coin(self.screen, self.sprites.spriteCollection, x, y))
        pass

    def addMushroom(self,x,y):
        pass
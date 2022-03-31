import json

with open("level_loc.txt", 'r') as f:
    rows = f.readlines()
    print(rows)

level11 = {
    "id":0,
    "length":200,
    "level": {
        "objects": {
            "bush": [],
            "sky": [],
            "cloud": [],
            "pipe":[],
            "ground":[]
        },
        "layers": {
            "sky": {
              "x": [0,200],
              "y": [0,13]
            },
            "ground": {
              "x": [0,200],
              "y": [14,16]
            }
        },
        "entites": {
            "randomBox": [],
            "coin": [],
            "Goomba":[],
            "Koopa":[]
        }
    }
}

rowCount = len(rows) - 1
colCount = 1

for string in rows:
    rowCount -= 1
    xy = [colCount,rowCount]
    # x,y coords
    for element in string:
        if element == " ":
            level11["level"]["objects"]["sky"].append(xy)
        if element == '?':
            # Item_Brick.png
            #self.addRandomBox(rowCount, colCount)
            level11["level"]["entites"]["randomBox"].append(xy)
        if element == 'G':
            # in allsprites
            level11["level"]["entites"]["Goomba"].append(xy)
            #self.addGoomba(rowCount, colCount)
        if element == 'X':
            # Ground_Brick.png
            level11["level"]["objects"]["ground"].append(xy)
            #self.addGroundBrick(rowCount, colCount)
        if element == 'R':
            pass
            # Stair_Brick.png

            #self.addStair(rowCount, colCount)
        if element == 'K':
            # in all sprites
            level11["level"]["entites"]["Koopa"].append(xy)
            #self.addKoopa(rowCount, colCount)
        if element == 'C':
            level11["level"]["entites"]["coin"].append(xy)
            # Coin.png
            #self.addCoin(rowCount, colCount)
        if element == 'M':
            pass
            # Mushroom.png
            #self.addMushroom(rowCount, colCount)
        if element == 'I':
            pass
            # Invisible_Block.png -> 1UP_Mushroom.png
            #self.invisableBlock(rowCount, colCount)
        if element == 'L':
            pass
            # Red_Brick.png -> Empty_Brick.png
            #self.addMultiHitBlock(rowCount, colCount)
        if element == 'S':
            pass
            # Red_Brick.png -> Star.png
            #self.addStar(rowCount, colCount)
        colCount += 1
        xy = [colCount, rowCount]
with open("../levels/Level1-1.json", "w") as outfile:
    json.dump(level11, outfile)
import json
image1 = {
    "x":24,
    "y":0,
    "scale":2
}

image2 = {
    "x":25,
    "y":0,
    "scale":2
}

image3 = {
    "x":26,
    "y":0,
    "scale":2
}

images = [image1, image2, image3]

randomBox = {
    "name": "randomBox",
    "images": images,
    "deltaTime": 10,
    "colorKey": None
}

image1 = {
    "x":24,
    "y":1,
    "scale":2
}

image2 = {
    "x":25,
    "y":1,
    "scale":2
}

image3 = {
    "x":26,
    "y":1,
    "scale":2
}

images = [image1, image2, image3]

coin = {
    "name": "coin",
    "images": images,
    "deltaTime": 10,
    "colorKey": -1
}

sprites = [randomBox,coin]

animation = {
    "spriteSheetURL": "./tiles.png",
    "type":"animation",
    "sprites": sprites
}

with open("Animation.json", "w") as outfile:
    json.dump(animation, outfile)

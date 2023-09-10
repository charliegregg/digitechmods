import math
import editor, nbt
from PIL import Image
import json



COLOURS = json.load(open("colours.json"))
for col in COLOURS:
    c = col["colour"]
    rgb = [int(c[:2],16),int(c[2:4],16),int(c[4:6],16), 255]
    if len(c)>6:
        rgb[-1] = int(c[6:],16)
    col["colour"] = rgb

def resample(img_data, w, pos):
    x0,y0 = math.floor(pos[0]),math.floor(pos[1])
    x1,y1 = x0+1,y0+1
    if y1*w<len(img_data):
        dx,dy = pos[0]-x0,pos[1]-y0
        vc = img_data[x0+y0*w], img_data[x1+y0*w], img_data[x0+y1*w], img_data[x1+y1*w]
        v = tuple(vc[0][i]*(1-dx)*(1-dy)+vc[1][i]*dx*(1-dy)+vc[2][i]*(1-dx)*dy+vc[3][i]*dx*dy for i in range(len(vc[0])))
        return v
    else:
        return img_data[x0+y0*w]

def closest_coloured_block(colour):
    lowest = math.inf
    best = None
    for col in COLOURS:
        c = col["colour"]
        if len(colour)==3 or colour[3]>0:
            if c[3]>250:
                # ht, st, vt = colorsys.rgb_to_hsv(*[t/256 for t in c[:3]])
                # hc, sc, vc = colorsys.rgb_to_hsv(*[t/256 for t in colour[:3]])
                # dist = (ht-hc)*(ht-hc)*4+(st-sc)*(st-sc)+(vt-vc)*(vt-vc)*2
                dist = sum((testchan-chan)**2 for testchan, chan in zip(c, colour))
            else:
                dist = math.inf
        else:
            dist = (c[3]-colour[3])**2
        if dist<lowest:
            best = col
            lowest = dist
    return nbt.convert_to_nbt({
        "version": {
            "NBT_TAG":"INT",
            "value":17959425
        },
        "name":"minecraft:"+best["block"],
        "states":best["states"]
    })


def im2str(imgfile, destfile, size=None, vertical=False):
    img = Image.open(imgfile)
    img_size = img.size
    print(img_size)
    img_data = list(img.convert("RGBA").getdata())
    img.close()
    if size is not None:
        img_data = [resample(img_data, img_size[0], (x/size[0]*img_size[0], y/size[1]*img_size[1])) for y in range(size[1]) for x in range(size[0])]
        img_size = size
    image_structure = editor.Structure()
    if vertical:
        image_structure.set_size(editor.vec3(img_size[0], img_size[1], 1))
    else:
        image_structure.set_size(editor.vec3(img_size[0], 1, img_size[1]))
    for x in range(img_size[0]):
        for y in range(img_size[1]):
            block = editor.Block(closest_coloured_block(img_data[x+y*img_size[0]]))
            if vertical:
                image_structure.set_block(block, editor.vec3(x, img_size[1]-y-1, 0))
            else:
                image_structure.set_block(block, editor.vec3(x, 0, y))
    nbt.encode_file(destfile, image_structure.to_nbt())
im2str("test.png", "test.mcstructure", vertical=True, size=(128,128))
# print(nbt.decode_file("nbttest.mcstructure")) # will show nbt data for test structure


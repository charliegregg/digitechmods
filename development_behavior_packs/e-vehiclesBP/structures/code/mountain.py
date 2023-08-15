import math, editor, solid, nbt, palette, pattern, random

class Mountain(solid.Solid):
    def __init__(self, height, radius):
        self.radius = radius
        self.height = height
        self.size = editor.vec3(radius*2+1, height, radius*2+1)

    def sample(self, pos):
        state = random.getstate()
        pos.x -= self.radius
        pos.z -= self.radius
        random.seed(hash((math.floor(pos.x),math.floor(pos.z))))
        offset = random.random()*self.height/self.radius
        random.setstate(state)
        return math.hypot(pos.x, pos.z)/self.radius*self.height + offset < self.height - pos.y
    
if __name__ == "__main__":
    border = Mountain(100, 15)
    border.create(palette.BORDER, pattern.Height, "../m/border.mcstructure")
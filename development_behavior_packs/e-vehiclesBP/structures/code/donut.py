import math, editor, solid, nbt, palette, pattern

class Donut(solid.Solid):
    def __init__(self, radius, thickness):
        self.radius = radius
        self.thickness = thickness
        self.size = editor.vec3(radius*2+1+thickness*2, radius*2+1+thickness*2, thickness*2)

    def sample(self, pos):
        pos.x -= self.radius + self.thickness
        pos.y -= self.radius + self.thickness
        pos.z -= self.thickness
        dist = math.hypot(pos.x, pos.y)
        if dist == 0:
            return False
        closest = (pos.x/dist*self.radius, pos.y/dist*self.radius)
        height = math.hypot(pos.x-closest[0], pos.y-closest[1], pos.z)
        if dist > self.radius and pos.y < 0: # in the base
            if pos.x < -self.radius:
                return math.hypot(pos.x+self.radius, 0, pos.z) < self.thickness
            if pos.x > self.radius:
                return math.hypot(pos.x-self.radius, 0, pos.z) < self.thickness
            return True
        return height < self.thickness
    
if __name__ == "__main__":
    donut = Donut(20, 5)
    donut.create(palette.BORDER, pattern.Height, "../m/donut.mcstructure")
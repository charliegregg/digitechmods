import math, editor, solid, nbt, palette, pattern, random, abc

class Radial(solid.Solid):
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

        y = pos.y/self.height
        d = math.hypot(pos.x, pos.z)/self.radius + offset/self.height
        return self.at(d, y)
    
    @abc.abstractmethod
    def at(self, d, y):
        ...
    
class Mountain(Radial):
    def at(self, d, y):
        return y < 1 - d
    
    
class Plateau(Radial):
    def at(self, d, y):
        return y < min(1,2 - 2*d)
    
class Rounded(Radial):
    def at(self, d, y):
        return y < 1-d*d
    
    
class Bowl(Radial):
    def at(self, d, y):
        d *= 1.316
        return y < 3/2*d*d - math.pow(d, 6)/2
    
if __name__ == "__main__":
    border = Mountain(100, 15)
    border.create(palette.BORDER, pattern.Height, "../m/border.mcstructure")
    borderp = Plateau(100, 15)
    borderp.create(palette.BORDER, pattern.Height, "../m/borderp.mcstructure")
    borderr = Rounded(100, 15)
    borderr.create(palette.BORDER, pattern.Height, "../m/borderr.mcstructure")
    bowl = Bowl(15, 35)
    bowl.create(palette.BORDER, pattern.Height, "../m/bowl.mcstructure")
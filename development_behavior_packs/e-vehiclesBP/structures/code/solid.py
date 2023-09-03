import math
import editor, nbt, palette, pattern
import json, random
import abc, tqdm

class Solid(abc.ABC):
    @abc.abstractmethod
    def sample(self, pos):
        pass
    
    def create(self, palette: palette.Palette, pattern: pattern.Pattern, destfile):
        structure = editor.Structure()
        structure.set_size(self.size)
        with tqdm.tqdm(total=self.size.x*self.size.y*self.size.z, desc=str(self.__class__.__name__)) as pbar:
            for x in range(self.size.x):
                for y in range(self.size.y):
                    for z in range(self.size.z):
                        pbar.update(1)
                        if self.sample(editor.vec3(x, y, z)):
                            if (percent := pattern.sample(editor.vec3(x/self.size.x, y/self.size.y, z/self.size.z))) >= 0:
                                structure.set_block(palette.get_block(percent), editor.vec3(x, y, z))
        nbt.encode_file(destfile, structure.to_nbt())


if __name__ == "__main__":
    pass
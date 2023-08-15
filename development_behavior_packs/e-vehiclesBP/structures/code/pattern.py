import math
import editor, nbt
import json, random
import abc

class Pattern(abc.ABC):
    @abc.abstractstaticmethod
    def sample(pos):
        pass

class Height(Pattern):
    def sample(pos):
        return pos.y

class Slice(Pattern):
    def sample(pos):
        return (pos.y+pos.x)/2
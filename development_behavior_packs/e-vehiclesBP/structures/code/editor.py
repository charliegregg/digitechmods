import formats
import nbt
import copy

class vec3:
    def __init__(self, x,y,z) -> None:
        self.x, self.y, self.z = x,y,z
    def __add__(self, other):
        return vec3(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self, other):
        return vec3(self.x-other.x,self.y-other.y,self.z-other.z)
    def __mul__(self, other):
        return vec3(self.x*other.x,self.y*other.y,self.z*other.z)
    def __div__(self, other):
        return vec3(self.x/other.x,self.y/other.y,self.z/other.z)
    def set(self, grid, obj):
        grid[self.x][self.y][self.z]=obj
    def get(self, grid):
        return grid[self.x][self.y][self.z]


class Structure:
    def __init__(self, json=None) -> None:
        self.size = vec3(1,1,1)
        self.layers = [[[[None]]],[[[None]]]]
        if json is not None:
            self.from_nbt(json)

    def set_size(self, size):
        for layer in [0,1]:
            self.layers[layer] = self.layers[layer][:size.x]+[[[None for _ in range(size.z)] for _ in range(size.y)] for _ in range(size.x)]
            for x in range(min(self.size.x, size.x)):
                self.layers[layer][x] = self.layers[layer][x][:size.y]+[[None for _ in range(size.z)] for _ in range(size.y)]
                for y in range(min(self.size.y, size.y)):
                    self.layers[layer][x][y] = self.layers[layer][x][y][:size.z]+[None for _ in range(size.z)]
        self.size=size

    def set_block(self, block, pos, layer=0):
        pos.set(self.layers[layer], block)

    def set_layer(self, layer, layer_number):
        self.layers[layer_number] = layer

    def get_layer(self, layer_number):
        return copy.deepcopy(self.layers[layer_number])

    def __add__(self, other):
        new = Structure()
        new.set_size(vec3(max(self.size.x,other.size.x), max(self.size.y, other.size.y), max(self.size.z, other.size.z)))
        new.set_layer(self.get_layer(0), 0)
        new.set_layer(other.get_layer(0), 1)
        return new
    merge=__add__

    def get_block(self, pos, layer):
        return pos.get(self.layers[layer])

    def to_nbt(self):
        main = copy.deepcopy(formats.STRUCTURE)
        main["size"]=nbt.LIST([nbt.INT(self.size.x), nbt.INT(self.size.y), nbt.INT(self.size.z)])
        for layer in [0,1]:
            block_num=0
            main["structure"]["block_indices"][layer]=nbt.LIST([-1]*(self.size.x*self.size.y*self.size.z))
            for x in range(self.size.x):
                for y in range(self.size.y):
                    for z in range(self.size.z):
                        block=self.get_block(vec3(x,y,z), layer)
                        if block is None:
                            main["structure"]["block_indices"][layer][block_num]=nbt.INT(-1)
                        else:
                            state = block.get_state()
                            data = block.get_data()
                            if state is not None:
                                if state not in main["structure"]["palette"]["default"]["block_palette"]:
                                    main["structure"]["palette"]["default"]["block_palette"].append(state)
                                    main["structure"]["block_indices"][layer][block_num]=nbt.INT(len(main["structure"]["palette"]["default"]["block_palette"])-1)
                                else:
                                    main["structure"]["block_indices"][layer][block_num]=nbt.INT(main["structure"]["palette"]["default"]["block_palette"].index(state))
                            else:
                                main["structure"]["block_indices"][layer][block_num]=nbt.INT(-1)
                            if data is not None:
                                main["structure"]["palette"]["default"]["block_position_data"][str(block_num)]=data
                        block_num+=1
        return main

    def from_nbt(self, main):
        self.set_size(vec3(*main["size"]))
        for layer in [0,1]:
            block_num=0
            for x in range(self.size.x):
                for y in range(self.size.y):
                    for z in range(self.size.z):
                        block = Block()
                        if main["structure"]["block_indices"][layer][block_num]!=-1:
                            state = main["structure"]["palette"]["default"]["block_palette"][main["structure"]["block_indices"][layer][block_num]]
                        else:
                            state = None
                        block.set_state(state)
                        if str(block_num) in main["structure"]["palette"]["default"]["block_position_data"]:
                            data = main["structure"]["palette"]["default"]["block_position_data"][str(block_num)]
                            block.set_data(data)
                        self.set_block(block, vec3(x,y,z), layer)
                        block_num+=1

class Block:
    def __init__(self, state=None, data=None) -> None:
        self.state=state
        self.data=data
    
    def set_state(self, state):
        self.state=state
    
    def set_data(self, data):
        self.data=data
    
    def get_state(self):
        return self.state
    
    def get_data(self):
        return self.data



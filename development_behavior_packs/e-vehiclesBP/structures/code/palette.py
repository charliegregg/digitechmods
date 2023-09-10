import editor, nbt
import random, json

class Palette:
    def __init__(self, data) -> None:
        self.data = data

    @staticmethod
    def to_block(block: str, states: dict) -> editor.Block:
        return editor.Block(nbt.convert_to_nbt({
            "version": {
                "NBT_TAG":"INT",
                "value":17959425
            },
            "name":block,
            "states":states
        }))

    def get_block(self, percent: float) -> editor.Block:
        possible = []
        weights = []
        for block in self.data:
            if block["start"] <= percent <= block["end"]:
                possible.append(block["block"])
                weights.append(block["weight"])
        block = random.choices(possible, weights)[0]
        if isinstance(block, dict):
            return self.to_block(block["name"], block["states"])
        return self.to_block(block, {})
    
    @staticmethod
    def load(file: str, spread: float = 1) -> "Palette":
        if file.endswith(".mcstructure"):
            data = []
            structure = editor.Structure(nbt.decode_file(file))
            if structure.size.x != 1:
                raise ValueError("Palette must be 1 x H x 1")
            if structure.size.z != 1:
                raise ValueError("Palette must be 1 x H x 1")
            for y in range(structure.size.y):
                block: editor.Block = structure.get_block(editor.vec3(0, y, 0), 0)
                data.append({
                    "start":(y-spread)/structure.size.y,
                    "end":(y+1+spread)/structure.size.y,
                    "block":block.get_state()["name"],
                    "states":block.get_state()["states"],
                    "weight":1
                })
            return Palette(data)
        return Palette(json.load(open(file)))
    
RAINBOW = Palette.load("../palettes/rainbow.mcstructure")

BORDER = Palette.load("../palettes/border.mcstructure", 0.01)

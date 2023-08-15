import struct, json
TAG_END=0
TAG_BYTE=1
TAG_SHORT=2
TAG_INT=3
TAG_LONG=4
TAG_FLOAT=5
TAG_DOUBLE=6
TAG_BYTE_ARRAY=7
TAG_STRING=8
TAG_LIST=9
TAG_COMPOUND=10
TAG_INT_ARRAY=11
TAG_LONG_ARRAY=12
class TAG:
    ID=-1
    def rep(self):
        if isinstance(self, list):
            return(f"{self.__class__.__name__}([{', '.join([val.rep() for val in self])}])")
        elif isinstance(self, dict):
            return(f"{self.__class__.__name__}({{{', '.join([f'{repr(k)}: {self[k].rep()}' for k in self])}}})")
        else:
            return(f"{self.__class__.__name__}({repr(self)})")
class END(TAG, int):
    ID=0
class BYTE(TAG, int):
    ID=1
class SHORT(TAG, int):
    ID=2
class INT(TAG, int):
    ID=3
class LONG(TAG, int):
    ID=4
class FLOAT(TAG, float):
    ID=5
class DOUBLE(TAG, float):
    ID=6
class BYTE_ARRAY(TAG, list):
    ID=7
class STRING(TAG, str):
    ID=8
class LIST(TAG, list):
    ID=9
class COMPOUND(TAG, dict):
    ID=10
class INT_ARRAY(TAG, list):
    ID=11
class LONG_ARRAY(TAG, list):
    ID=12
TAGS = TAG.__subclasses__()
NAME_TO_TAG = {tag.__name__:tag for tag in TAGS}
def decode_file(filename):
    with open(filename, "rb") as file:
        return _decode_tag(file)[1]

def encode_file(filename, value):
    with open(filename, "wb") as file:
        _encode_tag(file, "", value)

def _decode_tag(buffer):
    TAG_ID = int.from_bytes(buffer.read(1), byteorder="little")
    name_len = int.from_bytes(buffer.read(2), signed=False, byteorder="little")
    name = buffer.read(name_len).decode()
    value = DECODE_FUNCTIONS[TAG_ID](buffer)
    return(name, value)

def _encode_tag(buffer, name, value):
    TAG_ID = value.ID
    buffer.write(TAG_ID.to_bytes(1, "little"))
    name_bytes = name.encode()
    buffer.write(len(name_bytes).to_bytes(2, "little"))
    buffer.write(name_bytes)
    ENCODE_FUNCTIONS[TAG_ID](buffer, value)

def _decode_end(buffer):
    pass

def _encode_end(buffer, value:END):
    buffer.write(b"\x00")

def _decode_byte(buffer):
    value = int.from_bytes(buffer.read(1), byteorder="little", signed=True)
    return(BYTE(value))

def _encode_byte(buffer, value:BYTE):
    buffer.write(value.to_bytes(1, "little", signed=True))

def _decode_short(buffer):
    value = int.from_bytes(buffer.read(2), byteorder="little", signed=True)
    return(SHORT(value))

def _encode_short(buffer, value:SHORT):
    buffer.write(value.to_bytes(2, "little", signed=True))

def _decode_int(buffer):
    value = int.from_bytes(buffer.read(4), byteorder="little", signed=True)
    return(INT(value))

def _encode_int(buffer, value:INT):
    buffer.write(value.to_bytes(4, "little", signed=True))

def _decode_long(buffer):
    value = int.from_bytes(buffer.read(8), byteorder="little", signed=True)
    return(LONG(value))

def _encode_long(buffer, value:LONG):
    buffer.write(value.to_bytes(8, "little", signed=True))

def _decode_float(buffer):
    value = struct.unpack('>f', buffer.read(4))[0]
    return(FLOAT(value))

def _encode_float(buffer, value:FLOAT):
    buffer.write(struct.pack('>f', value))

def _decode_double(buffer):
    value = struct.unpack('>d', buffer.read(8))[0]
    return(DOUBLE(value))

def _encode_double(buffer, value:DOUBLE):
    buffer.write(struct.pack('>d', value))
    
def _decode_byte_array(buffer):
    value = []
    LENGTH = int.from_bytes(buffer.read(4), byteorder="little")
    for _ in range(LENGTH):
        value += _decode_byte(buffer)
    return(BYTE_ARRAY(value))

def _encode_byte_array(buffer, value:BYTE_ARRAY):
    buffer.write(len(value).to_bytes(4, "little"))
    for tag in value:
        if isinstance(tag, BYTE):
            _encode_byte(buffer, tag)
        else:
            _encode_byte(buffer, BYTE(tag))
    
def _decode_string(buffer):
    string_len = int.from_bytes(buffer.read(2), signed=False, byteorder="little")
    value = buffer.read(string_len).decode()
    return(STRING(value))
    
def _encode_string(buffer, value:STRING):
    string_bytes = value.encode()
    buffer.write(len(string_bytes).to_bytes(2, "little", signed=False))
    buffer.write(string_bytes)

def _decode_list(buffer):
    value = []
    TAG_ID = int.from_bytes(buffer.read(1), byteorder="little")
    LENGTH = int.from_bytes(buffer.read(4), byteorder="little")
    for _ in range(LENGTH):
        value.append(DECODE_FUNCTIONS[TAG_ID](buffer))
    l=LIST(value)
    l.type=TAG_ID
    return(l)

def _encode_list(buffer, value:LIST):
    if hasattr(value, "type"):
        TAG_ID=value.type
    elif value:
        TAG_ID = value[0].ID
    else:
        TAG_ID=0
    for tag in value:
        if TAG_ID!=tag.ID:
            raise TypeError(f"list '{value}' cannot contain types otherthan '{value.type}'")
    buffer.write(TAG_ID.to_bytes(1, "little"))
    buffer.write(len(value).to_bytes(4, "little"))
    for tag in value:
        ENCODE_FUNCTIONS[TAG_ID](buffer, tag)

def _decode_compound(buffer):
    value = {}
    while int.from_bytes(buffer.read(1), byteorder="little")!=0:
        buffer.seek(-1, 1)
        k, v = _decode_tag(buffer)
        value[k] = v
    return(COMPOUND(value))

def _encode_compound(buffer, value):
    for n in value:
        _encode_tag(buffer, n, value[n])
    _encode_end(buffer, END())

def _decode_int_array(buffer):
    value = []
    LENGTH = int.from_bytes(buffer.read(4), byteorder="little")
    for _ in range(LENGTH):
        value.append(_decode_int(buffer))
    return(INT_ARRAY(value))

def _encode_int_array(buffer, value):
    buffer.write(len(value).to_bytes(4, "little"))
    for tag in value:
        if isinstance(tag, INT):
            _encode_int(buffer, tag)
        else:
            _encode_int(buffer, INT(tag))

def _decode_long_array(buffer):
    value = []
    LENGTH = int.from_bytes(buffer.read(4), byteorder="little",)
    for _ in range(LENGTH):
        value += _decode_long(buffer)
    return(LONG_ARRAY(value))

def _encode_long_array(buffer, value):
    buffer.write(len(value).to_bytes(4, "little"))
    for tag in value:
        if isinstance(tag, LONG):
            _encode_long(buffer, tag)
        else:
            _encode_long(buffer, LONG(tag))


def convert_to_nbt(value):
    if isinstance(value, dict):
        if "NBT_TAG" in value:
            return NAME_TO_TAG[value["NBT_TAG"]](value["value"])
        return COMPOUND({k:convert_to_nbt(v) for k, v in value.items()})
    elif isinstance(value, list):
        return LIST([convert_to_nbt(v) for v in value])
    elif isinstance(value, float):
        return FLOAT(value)
    elif isinstance(value, int):
        return INT(value)
    elif isinstance(value, str):
        return STRING(value)
    else:
        return BYTE(0)


DECODE_FUNCTIONS=[_decode_end, _decode_byte, _decode_short, _decode_int, _decode_long, _decode_float, _decode_double, _decode_byte_array, _decode_string, _decode_list, _decode_compound, _decode_int_array, _decode_long_array]
ENCODE_FUNCTIONS=[_encode_end, _encode_byte, _encode_short, _encode_int, _encode_long, _encode_float, _encode_double, _encode_byte_array, _encode_string, _encode_list, _encode_compound, _encode_int_array, _encode_long_array]

if __name__=="__main__":
    path = "/Users/charlie_gregg25/Library/Application Support/minecraftpe/games/com.mojang/minecraftWorlds/BB-BZHYmAQA=/level.dat"
    with open(path, "rb") as file:
        extra = file.read(8)
        data = _decode_tag(file)[1]
    with open("decoded.json", "w") as file:
        json.dump(data, file, indent=4)
    data["experiments"]["upcoming_creator_features"] = BYTE(1)
    data["experiments"]["experimental_molang_features"] = BYTE(1)
    data["experiments"]["data_driven_items"] = BYTE(1)
    data["experiments"]["experiments_ever_used"] = BYTE(1)
    data["experiments"]["saved_with_toggled_experiments"] = BYTE(1)
    with open("encoded.dat", "wb") as file:
        file.write(extra)
        _encode_tag(file, "", data)
from nbt import *
STRUCTURE = COMPOUND({
    'format_version': INT(1), 
    'size': LIST([INT(1), INT(1), INT(1)]), 
    'structure': COMPOUND({
        'block_indices': LIST([LIST([INT(-1)]), LIST([INT(-1)])]), 
        'entities': LIST([]), 
        'palette': COMPOUND({
            'default': COMPOUND({
                'block_palette': LIST([]), 
                'block_position_data': COMPOUND({})})})}), 
    'structure_world_origin': LIST([INT(0), INT(0), INT(0)])})
ITEM = COMPOUND({'Count': BYTE(1), 'Damage': SHORT(0), 'Name': STRING('minecraft:air'), 'Slot': BYTE(0), 'WasPickedUp': BYTE(0), 'tag': COMPOUND({})})
ENCHANTMENT = {'ench': LIST([COMPOUND({'id': SHORT(9), 'lvl': SHORT(1)})])}
DOUBLE_GRASS = COMPOUND({'format_version': INT(1), 'size': LIST([INT(1), INT(1), INT(1)]), 'structure': COMPOUND({'block_indices': LIST([LIST([INT(0)]), LIST([INT(1)])]), 'entities': LIST([]), 'palette': COMPOUND({'default': COMPOUND({'block_palette': LIST([COMPOUND({'name': STRING('minecraft:chest'), 'states': COMPOUND({'facing_direction': INT(4)}), 'version': INT(17879555)}), COMPOUND({'name': STRING('minecraft:grass'), 'states': COMPOUND({}), 'version': INT(17879555)})]), 'block_position_data': COMPOUND({})})})}), 'structure_world_origin': LIST([INT(-48), INT(-59), INT(23)])})

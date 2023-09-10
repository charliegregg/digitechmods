scoreboard objectives add math dummy

function ev/car/tick
function ev/race/tick
function ev/race_build/tick

execute @e[type=item,name="Plastic Bottle"] ~ ~ ~ detect ~ ~-1 ~ cg:recycle -1 give @p cg:fabric 1
execute @e[type=item,name="Plastic Bottle"] ~ ~ ~ detect ~ ~-1 ~ cg:recycle -1 kill @s

effect @a night_vision 1000000 0 true
effect @a saturation 1000000 0 true
effect @a resistance 1000000 0 true
effect @a fire_resistance 1000000 0 true
effect @a water_breathing 1000000 0 true
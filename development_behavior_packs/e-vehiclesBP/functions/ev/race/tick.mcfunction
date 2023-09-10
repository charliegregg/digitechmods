scoreboard objectives add race_start dummy
scoreboard objectives add race_time dummy
scoreboard objectives add checkp dummy
scoreboard objectives add raceid dummy
scoreboard objectives add racescore dummy

function ev/race/tick_start
function ev/race/tick_death

scoreboard players add @e[tag=racing] race_time 1
execute @e[type=cg:car,tag=racing] ~ ~ ~ function ev/race/mini_time
execute @e[type=cg:car,tag=racing] ~ ~ ~ function ev/race/tick_checkp
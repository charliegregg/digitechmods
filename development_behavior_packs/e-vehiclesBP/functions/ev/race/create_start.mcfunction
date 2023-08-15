
summon cg:race_start_marker
scoreboard players add next raceid 1
scoreboard players operation @e[type=cg:race_start_marker,c=1] raceid = next raceid
scoreboard players set next checkp 0
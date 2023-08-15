title @a[r=3] title §l§cYou lost!
scoreboard players operation @e[type=cg:race_start_marker] raceid -= @s raceid
tp @a[r=3] @e[type=cg:race_start_marker,scores={raceid=0}]
tp @e[type=cg:race_start_marker,scores={raceid=0}]
scoreboard players operation @e[type=cg:race_start_marker] raceid += @s raceid
# ride @a[r=3] start_riding @s teleport_rider
tag @s remove racing
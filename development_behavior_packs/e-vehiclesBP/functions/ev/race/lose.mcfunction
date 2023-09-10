execute @s ^ ^0.3 ^0.6 title @p[r=3] title §l§cYou lost!
scoreboard players operation @e[type=cg:race_start_marker] raceid -= @s raceid
execute @s ^ ^0.3 ^0.6 tp @p[r=3] @e[type=cg:race_start_marker,scores={raceid=0}]
tp @e[type=cg:race_start_marker,scores={raceid=0}]
scoreboard players operation @e[type=cg:race_start_marker] raceid += @s raceid

tag @s remove racing
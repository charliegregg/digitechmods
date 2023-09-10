scoreboard players add @e[tag=starting_race] race_start 1
execute @e[tag=starting_race,scores={race_start=1}] ~ ~ ~ execute @e[type=cg:race_start_barrier_marker] ~ ~ ~ fill ~ ~ ~ ~ ~1 ~ minecraft:barrier
execute @e[tag=starting_race,scores={race_start=1}] ~ ~ ~ titleraw @a[r=20] title {"rawtext":[{"text":"§c3"}]}
execute @e[tag=starting_race,scores={race_start=1}] ~ ~ ~ playsound random.toast @a[r=20] ~ ~ ~ 1 1
execute @e[tag=starting_race,scores={race_start=1}] ~ ~ ~ execute @e[type=cg:race_light_marker,r=20] ~ ~ ~ setblock ~ ~ ~ minecraft:red_nether_brick
execute @e[tag=starting_race,scores={race_start=21}] ~ ~ ~ titleraw @a[r=20] title {"rawtext":[{"text":"§62"}]}
execute @e[tag=starting_race,scores={race_start=21}] ~ ~ ~ playsound random.toast @a[r=20] ~ ~ ~ 1 1
execute @e[tag=starting_race,scores={race_start=21}] ~ ~ ~ execute @e[type=cg:race_light_marker,r=20] ~ ~ ~ setblock ~ ~ ~ minecraft:redstone_block
execute @e[tag=starting_race,scores={race_start=41}] ~ ~ ~ titleraw @a[r=20] title {"rawtext":[{"text":"§e1"}]}
execute @e[tag=starting_race,scores={race_start=41}] ~ ~ ~ playsound random.toast @a[r=20] ~ ~ ~ 1 1
execute @e[tag=starting_race,scores={race_start=41}] ~ ~ ~ execute @e[type=cg:race_light_marker,r=20] ~ ~ ~ setblock ~ ~ ~ minecraft:gold_block
execute @e[tag=starting_race,scores={race_start=61}] ~ ~ ~ titleraw @a[r=20] title {"rawtext":[{"text":"§aGO"}]}
execute @e[tag=starting_race,scores={race_start=61}] ~ ~ ~ playsound random.toast @a[r=20] ~ ~ ~ 1 2
execute @e[tag=starting_race,scores={race_start=61}] ~ ~ ~ execute @e[type=cg:race_light_marker,r=20] ~ ~ ~ setblock ~ ~ ~ minecraft:emerald_block
execute @e[tag=starting_race,scores={race_start=61}] ~ ~ ~ execute @e[type=cg:race_start_barrier_marker] ~ ~ ~ fill ~ ~ ~ ~ ~1 ~ minecraft:air
execute @e[tag=starting_race,scores={race_start=61}] ~ ~ ~ tag @e[type=cg:car,r=20] add racing
execute @e[tag=starting_race,scores={race_start=61}] ~ ~ ~ scoreboard players set @e[type=cg:car,r=20] race_time 0
execute @e[tag=starting_race,scores={race_start=61}] ~ ~ ~ scoreboard players set @e[type=cg:car,r=20] checkp 0
execute @e[tag=starting_race,scores={race_start=61}] ~ ~ ~ scoreboard players operation @e[type=cg:car,r=20] raceid = @s raceid
execute @e[tag=starting_race,scores={race_start=61}] ~ ~ ~ function ev/race/display_start
execute @e[tag=starting_race,scores={race_start=81}] ~ ~ ~ execute @e[type=cg:race_light_marker,r=20] ~ ~ ~ setblock ~ ~ ~ minecraft:coal_block
execute @e[tag=starting_race,scores={race_start=81}] ~ ~ ~ tag @s remove starting_race
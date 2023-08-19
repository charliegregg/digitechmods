scoreboard objectives add charge_time dummy
scoreboard objectives add charge dummy

execute @e[tag=cg_charging,scores={charge=200..}] ~ ~ ~ function ev/car/charged
effect @e[tag=cg_charging] slowness 1 255 true
effect @e[type=cg:car,scores={charge=..0}] slowness 1 5 true
scoreboard players add @e[tag=cg_charging] charge 1

scoreboard players add @e[tag=move,scores={charge=1..}] charge_time 1
execute @e[tag=move,scores={charge_time=20..}] ~ ~ ~ scoreboard players remove @s charge 1
tag @e[tag=stop_move] remove move
tag @e[tag=stop_move] remove stop_move
scoreboard players set @e[tag=move,scores={charge_time=20..}] charge_time 0

execute @e[type=cg:car,scores={charge=150..}] ~ ~ ~ titleraw @a[r=3,tag=!racing] actionbar {"rawtext":[{"text":"§a§lCHARGE: §2"}, {"score":{"name":"@s","objective":"charge"}},{"text":"§a/200"}]}
execute @e[type=cg:car,scores={charge=100..149}] ~ ~ ~ titleraw @a[r=3,tag=!racing] actionbar {"rawtext":[{"text":"§e§lCHARGE: §a"}, {"score":{"name":"@s","objective":"charge"}},{"text":"§e/200"}]}
execute @e[type=cg:car,scores={charge=50..99}] ~ ~ ~ titleraw @a[r=3,tag=!racing] actionbar {"rawtext":[{"text":"§6§lCHARGE: §e"}, {"score":{"name":"@s","objective":"charge"}},{"text":"§6/200"}]}
execute @e[type=cg:car,scores={charge=0..49}] ~ ~ ~ titleraw @a[r=3,tag=!racing] actionbar {"rawtext":[{"text":"§c§lCHARGE: §6"}, {"score":{"name":"@s","objective":"charge"}},{"text":"§c/200"}]}

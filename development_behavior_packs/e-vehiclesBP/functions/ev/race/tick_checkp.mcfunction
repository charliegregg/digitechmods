
tag @s add this
execute @s ^ ^ ^-5 tag @e[type=cg:checkpoint,r=5] add test_checkp
scoreboard players operation @e[tag=test_checkp] raceid -= @s raceid
scoreboard players operation @e[tag=test_checkp] checkp -= @s checkp
# the next checkpoint in this race
execute @e[tag=test_checkp,scores={checkp=1,raceid=0},tag=!finish] ~ ~ ~ tag @e[tag=this] add nextcp
execute @e[tag=test_checkp,scores={checkp=1,raceid=0},tag=finish] ~ ~ ~ tag @e[tag=this] add win
scoreboard players operation @e[tag=test_checkp] raceid += @s raceid
scoreboard players operation @e[tag=test_checkp] checkp += @s checkp
tag @e remove test_checkp



execute @s[tag=nextcp] ~ ~ ~ scoreboard players add @s checkp 1
execute @s[tag=nextcp] ^ ^0.3 ^0.6 playsound random.levelup @p[r=3]
execute @s[tag=nextcp] ~ ~ ~ particle minecraft:huge_explosion_emitter ^ ^ ^5
execute @s[tag=win] ~ ~ ~ tag @p add winner
execute @s[tag=win] ~ ~ ~ function ev/race/calculate_time
execute @s[tag=win] ~ ~ ~ function ev/race/calculate_score
execute @s[tag=win] ~ ~ ~ function ev/race/display_time
execute @s[tag=win] ^ ^0.3 ^0.6 playsound random.levelup @p[r=3] ~ ~ ~ 1 1.5
tag @s[tag=win] remove racing
tag @a remove winner
tag @s remove nextcp
tag @s remove win
tag @s remove this
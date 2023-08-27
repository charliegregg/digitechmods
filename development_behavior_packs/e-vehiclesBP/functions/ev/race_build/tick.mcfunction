execute @a[hasitem={item=cg:track_builder,location=slot.weapon.mainhand}] ~ ~ ~ tag @s add track_builder
execute @a[hasitem={item=cg:track_builder,location=slot.weapon.mainhand,quantity=0}] ~ ~ ~ tag @s remove track_builder
execute @a[hasitem={item=cg:track_mover,location=slot.weapon.mainhand}] ~ ~ ~ tp @e[type=cg:track_trailer,c=1] ~ ~0.5 ~
execute @e[type=cg:track_trailer] ~ ~ ~ particle minecraft:basic_flame_particle ~ ~ ~
execute @a[tag=track_builder] ~ ~ ~ execute @e[type=cg:track_trailer,rm=10,r=30,c=1] ~ ~ ~ tp ~ ~ ~ facing @p[tag=track_builder]
execute @a[tag=track_builder] ~ ~ ~ execute @e[type=cg:track_trailer,rm=10,r=30,c=1] ~ ~ ~ tp ^ ^ ^0.5 facing @p[tag=track_builder]
execute @a[tag=track_builder] ~ ~ ~ execute @e[type=cg:track_trailer,c=1] ~ ~-1 ~ function ev/race_build/section
execute @a[hasitem={item=cg:track_deletor,location=slot.weapon.mainhand}] ~ ~ ~ fill ~-6 ~ ~-6 ~6 ~10 ~6 air
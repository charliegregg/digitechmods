# floor
setblock ^-4.5 ^ ^ gray_concrete
setblock ^-4   ^ ^ gray_concrete
setblock ^-3.5 ^ ^ gray_concrete
setblock ^-3   ^ ^ gray_concrete
setblock ^-2.5 ^ ^ gray_concrete
setblock ^-2   ^ ^ gray_concrete
setblock ^-1.5 ^ ^ gray_concrete
setblock ^-1   ^ ^ gray_concrete
setblock ^-0.5 ^ ^ gray_concrete
setblock ^     ^ ^ gray_concrete
setblock ^0.5  ^ ^ gray_concrete
setblock ^1    ^ ^ gray_concrete
setblock ^1.5  ^ ^ gray_concrete
setblock ^2    ^ ^ gray_concrete
setblock ^2.5  ^ ^ gray_concrete
setblock ^3    ^ ^ gray_concrete
setblock ^3.5  ^ ^ gray_concrete
setblock ^4    ^ ^ gray_concrete
setblock ^4.5  ^ ^ gray_concrete
# floor back half block to fill gaps
setblock ^-4.5 ^ ^-0.5 gray_concrete
setblock ^-4   ^ ^-0.5 gray_concrete
setblock ^-3.5 ^ ^-0.5 gray_concrete
setblock ^-3   ^ ^-0.5 gray_concrete
setblock ^-2.5 ^ ^-0.5 gray_concrete
setblock ^-2   ^ ^-0.5 gray_concrete
setblock ^-1.5 ^ ^-0.5 gray_concrete
setblock ^-1   ^ ^-0.5 gray_concrete
setblock ^-0.5 ^ ^-0.5 gray_concrete
setblock ^     ^ ^-0.5 gray_concrete
setblock ^0.5  ^ ^-0.5 gray_concrete
setblock ^1    ^ ^-0.5 gray_concrete
setblock ^1.5  ^ ^-0.5 gray_concrete
setblock ^2    ^ ^-0.5 gray_concrete
setblock ^2.5  ^ ^-0.5 gray_concrete
setblock ^3    ^ ^-0.5 gray_concrete
setblock ^3.5  ^ ^-0.5 gray_concrete
setblock ^4    ^ ^-0.5 gray_concrete
setblock ^4.5  ^ ^-0.5 gray_concrete
# walls
setblock ^-4.5 ^1 ^ minecraft:quartz_block 3
setblock ^-4.5 ^1.5 ^ minecraft:quartz_block 3
setblock ^-4.5 ^2 ^ minecraft:barrier
setblock ^-4.5 ^2.5 ^ minecraft:barrier
setblock ^4.5  ^1 ^ minecraft:quartz_block 3
setblock ^4.5  ^1.5 ^ minecraft:quartz_block 3
setblock ^4.5  ^2 ^ minecraft:barrier
setblock ^4.5  ^2.5 ^ minecraft:barrier
# extra barriers
execute @s ^-4.5 ^ ^     fill ~ ~2 ~ ~ ~5 ~ minecraft:barrier 0 replace air
execute @s ^4.5  ^ ^     fill ~ ~2 ~ ~ ~5 ~ minecraft:barrier 0 replace air
execute @s ^-4.5 ^ ^-0.5 fill ~ ~2 ~ ~ ~5 ~ minecraft:barrier 0 replace air
execute @s ^4.5  ^ ^-0.5 fill ~ ~2 ~ ~ ~5 ~ minecraft:barrier 0 replace air
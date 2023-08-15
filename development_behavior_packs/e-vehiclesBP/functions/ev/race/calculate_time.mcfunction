scoreboard players operation seconds math = @s race_time
scoreboard players set op math 20
scoreboard players operation seconds math /= op math
scoreboard players operation hundredths math = @s race_time
scoreboard players operation hundredths math %= op math
scoreboard players set op math 5
scoreboard players operation hundredths math *= op math
scoreboard players operation tenths math = hundredths math
scoreboard players set op math 10
scoreboard players operation hundredths math %= op math
scoreboard players operation tenths math /= op math
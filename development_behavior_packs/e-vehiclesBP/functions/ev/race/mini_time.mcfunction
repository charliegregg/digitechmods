function ev/race/calculate_time
titleraw @a[r=3] actionbar { "rawtext": [{"text":"§eCP: §a"},{"score":{"name":"@s","objective":"checkp"}}, {"text": " §c"}, { "score": {"name": "seconds", "objective": "math" } }, {"text": "."}, { "score": {"name": "tenths", "objective": "math" } }, { "score": {"name": "hundredths", "objective": "math" } }, { "text": "s" }] }
execute @s[scores={raceid=1}] ~ ~ ~ titleraw @a[r=3] actionbar { "rawtext": [{"text":"§dLazy Loop §b- §eCP: §a"},{"score":{"name":"@s","objective":"checkp"}}, {"text": " §c"}, { "score": {"name": "seconds", "objective": "math" } }, {"text": "."}, { "score": {"name": "tenths", "objective": "math" } }, { "score": {"name": "hundredths", "objective": "math" } }, { "text": "s" }] }
execute @s[scores={raceid=2}] ~ ~ ~ titleraw @a[r=3] actionbar { "rawtext": [{"text":"§dTreacherous Turns §b- §eCP: §a"},{"score":{"name":"@s","objective":"checkp"}}, {"text": " §c"}, { "score": {"name": "seconds", "objective": "math" } }, {"text": "."}, { "score": {"name": "tenths", "objective": "math" } }, { "score": {"name": "hundredths", "objective": "math" } }, { "text": "s" }] }
execute @s[scores={raceid=3}] ~ ~ ~ titleraw @a[r=3] actionbar { "rawtext": [{"text":"§dLong Line §b- §eCP: §a"},{"score":{"name":"@s","objective":"checkp"}}, {"text": " §c"}, { "score": {"name": "seconds", "objective": "math" } }, {"text": "."}, { "score": {"name": "tenths", "objective": "math" } }, { "score": {"name": "hundredths", "objective": "math" } }, { "text": "s" }] }
execute @s[scores={raceid=4}] ~ ~ ~ titleraw @a[r=3] actionbar { "rawtext": [{"text":"§dStrict Strips §b- §eCP: §a"},{"score":{"name":"@s","objective":"checkp"}}, {"text": " §c"}, { "score": {"name": "seconds", "objective": "math" } }, {"text": "."}, { "score": {"name": "tenths", "objective": "math" } }, { "score": {"name": "hundredths", "objective": "math" } }, { "text": "s" }] }

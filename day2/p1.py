import re

with open("input", encoding="utf-8") as file:
    content = file.readlines()

# 12 red 13 green 14 blue
result = 0
for game in content:
    game_id = int(re.findall(r"Game \d+", game)[0][5:])
    print(game_id)
    red = max(int(example[:-4]) for example in re.findall(r'\d+ red', game))
    green = max(int(example[:-6]) for example in re.findall(r'\d+ green', game))
    blue = max(int(example[:-5]) for example in re.findall(r'\d+ blue', game))
    if red <= 12 and green <= 13 and blue <= 14:
        result += game_id

print(result)

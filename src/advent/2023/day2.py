from functools import reduce
import math
from operator import mul
from advent.load import read_input

data = read_input(group=True)[0]

bag_totals = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def game_id_and_cube_list(game_str):
    colon_idx = game_str.find(":")
    game_id = int(game_str[[x.isdigit() for x in game_str].index(True):colon_idx])
    cube_list = game_str[colon_idx+2:]

    return (game_id, cube_list)

def game_id_if_possible(game_str: str) -> int:
    game_id, cube_list = game_id_and_cube_list(game_str)
    return int(game_id) if is_possible(cube_list) else 0

def is_possible(cube_sets: str) -> bool:
    for handful in cube_sets.split("; "):
        for cubes in handful.split(", "):
            count, color = cubes.split(" ")
            if int(count) > bag_totals[color]:
                return False
    return True

def game_as_dicts(cube_sets: str) -> bool:
    game_map = []
    for set in cube_sets.split("; "):
        set_dict = {}
        for cubes in set.split(", "):
            count, color = cubes.split(" ")
            set_dict[color] = count
        game_map.append(set_dict)
    by_color = collect_by_color(game_map)
    power = reduce(mul, by_color.values())
    return power
    

def collect_by_color(game_map):
    result_dict = {}
    for d in game_map:
        for key, value in d.items():
            if key not in result_dict or int(value) > result_dict[key]:
                result_dict[key] = int(value)
    return result_dict


print(sum([game_id_if_possible(game) for game in data]))
print(sum([game_as_dicts(game_id_and_cube_list(game)[1]) for game in data]))

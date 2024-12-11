from functools import lru_cache

# with open('day11_test_input.txt') as f:
with open('day11_input.txt') as f:
    data = f.read()

stones = [int(i) for i in data.strip('\n').split(' ')]

@lru_cache(maxsize=1000)
def evolve_stone(stone):
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        new_stone_a = int(str(stone)[:len(str(stone)) // 2])
        new_stone_b = int(str(stone)[len(str(stone)) // 2:])
        return [new_stone_a, new_stone_b]

    return [stone * 2024]

# def evolve_stone_fully(stone_initial, num_blinks=75):
#     # stones_evolution = {}
#     stones = [stone_initial]
#     for blink_i in range(0, num_blinks):
#         print(blink_i)
#         # stones_evolution[blink_i] = len(stones)
#         new_stones = []
#         for stone in stones:
#             new_stones.extend(evolve_stone(stone))
#         stones = copy(new_stones)
#
#     return len(stones)

# def evolve_stone_fully(stone_initial, num_blinks=75):
#     # stones_evolution = {}
#     stones = [stone_initial]
#     for blink_i in range(0, num_blinks):
#         print(blink_i)
#         # stones_evolution[blink_i] = len(stones)
#         new_stones = []
#         for stone in stones:
#             new_stones.extend(evolve_stone(stone))
#         stones = copy(new_stones)
#
#     return len(stones)


@lru_cache(maxsize=1000)
def evolve_stone_recursive(stone_initial, blinks_remaining):
    if blinks_remaining == 0:
        return 1
    else:
        num_stones = 0
        new_stones = evolve_stone(stone_initial)
        for stone in new_stones:
            num_stones += evolve_stone_recursive(stone, blinks_remaining-1)
        return num_stones

total_stone_count = 0
for stone in stones:
    print(stone)
    total_stone_count += evolve_stone_recursive(stone, blinks_remaining=75)

print(total_stone_count)
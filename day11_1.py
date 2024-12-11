from copy import copy

# with open('day11_test_input.txt') as f:
with open('day11_input.txt') as f:
    data = f.read()

stones = [int(i) for i in data.strip('\n').split(' ')]

def evolve_stone(stone):
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        new_stone_a = int(str(stone)[:len(str(stone)) // 2])
        new_stone_b = int(str(stone)[len(str(stone)) // 2:])
        return [new_stone_a, new_stone_b]

    return [stone * 2024]


for blink_i in range(0, 25):
    new_stones = []
    for stone in stones:
        new_stones.extend(evolve_stone(stone))

    stones = copy(new_stones)

print(len(stones))
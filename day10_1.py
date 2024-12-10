import numpy as np
from heapq import heappush, heappop

# with open('day10_test_input.txt') as f:
with open('day10_input.txt') as f:
    data = f.read()

lines = data.strip('\n').split('\n')
dataarray = []
for line in lines:
    dataarray.append([int(i) for i in line])
np_array = np.array(dataarray)

x, y = np.where(np_array == 0)
trailhead_positions = [(i, j) for i, j in zip(x, y)]

def get_possible_next_steps(pos, grid):
    nrows = grid.shape[0]
    ncols = grid.shape[1]
    available_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if pos[0] == 0:
        available_directions.remove((-1, 0))
    if pos[1] == 0:
        available_directions.remove((0, -1))
    if pos[0] == nrows - 1:
        available_directions.remove((1, 0))
    if pos[1] == ncols - 1:
        available_directions.remove((0, 1))

    current_pos_value = grid[pos]
    possible_next_steps = []
    for direction in available_directions:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        next_pos_value = grid[next_pos]
        if next_pos_value - current_pos_value == 1:
            possible_next_steps.append(next_pos)

    return possible_next_steps

overall_score = 0
for trailhead_position in trailhead_positions:
    trailhead_score = 0
    reachable_trail_ends = []
    paths = [trailhead_position]

    while len(paths) > 0:
        position = heappop(paths)

        if np_array[position] == 9 and position not in reachable_trail_ends:
            trailhead_score += 1
            reachable_trail_ends.append(position)
            continue

        possible_next_steps = get_possible_next_steps(position, np_array)
        for next_step in possible_next_steps:
            heappush(paths, next_step)

    overall_score += trailhead_score

print(overall_score)
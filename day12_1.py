from collections import defaultdict
import numpy as np

# with open('day12_test_input_1.txt') as f:
# with open('day12_test_input_2.txt') as f:
# with open('day12_test_input_3.txt') as f:
with open('day12_input.txt') as f:
    data = f.read()

lines = data.strip('\n').split('\n')
dataarray = []
for line in lines:
    dataarray.append([i for i in line])
np_array = np.array(dataarray)

def check_neighbours(pos, grid):
    nrows = grid.shape[0]
    ncols = grid.shape[1]
    available_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # if pos[0] == 0:
    #     available_directions.remove((-1, 0))
    # if pos[1] == 0:
    #     available_directions.remove((0, -1))
    # if pos[0] == nrows - 1:
    #     available_directions.remove((1, 0))
    # if pos[1] == ncols - 1:
    #     available_directions.remove((0, 1))

    fences_needed = []
    same_type_neighbours = []
    this_pos_type = grid[pos]
    for direction in available_directions:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if (next_pos[0] < 0) or (next_pos[0] >= ncols) or (next_pos[1] < 0) or (next_pos[1] >= nrows):
            fences_needed.append((pos, next_pos))
            continue

        next_pos_type = grid[next_pos]
        if this_pos_type == next_pos_type:
            same_type_neighbours.append(next_pos)
        # if this_pos_type != next_pos_type:
        else:
            fences_needed.append((pos, next_pos))
            # fences_needed.append((next_pos, pos))

    return same_type_neighbours, fences_needed

# all_fences_needed = defaultdict(list)
all_fences_needed = defaultdict(int)
areas = defaultdict(int)
checked_positions = []
region_num = 0
for i in range(0, np_array.shape[0]):
    for j in range(0, np_array.shape[0]):
        if (i, j) in checked_positions:
            continue

        region_positions = [(i, j)]
        while len(region_positions) > 0:
            pos = region_positions.pop()
            if pos in checked_positions:
                continue
            checked_positions.append(pos)
            # print(pos)
            same_type_neighbours, fences_needed = check_neighbours(pos, np_array)
            # pos_type = np_array[(i, j)]
            # all_fences_needed[pos_type].extend(fences_needed)
            # all_fences_needed[pos_type] += len(fences_needed) # extend(fences_needed)
            # areas[pos_type] += 1
            all_fences_needed[region_num] += len(fences_needed)
            areas[region_num] += 1
            region_positions.extend(same_type_neighbours)

        region_num += 1

total_price = 0
for region in all_fences_needed:
    price = all_fences_needed[region] * areas[region]
    total_price += price

print(total_price)

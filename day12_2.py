from collections import defaultdict
from copy import copy
import numpy as np

# with open('day12_test_input_1.txt') as f:
# with open('day12_test_input_2.txt') as f:
# with open('day12_test_input_3.txt') as f:
# with open('day12_test_input_4.txt') as f:
# with open('day12_test_input_5.txt') as f:
with open('day12_input.txt') as f:
    data = f.read()

lines = data.strip('\n').split('\n')
dataarray = []
for line in lines:
    dataarray.append([i for i in line])
np_array = np.array(dataarray)

# x, y = np.where(np_array == 0)
# trailhead_positions = [(i, j) for i, j in zip(x, y)]

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
region_positions_dict = defaultdict(list)
regions_perimeter_squares = defaultdict(list)
checked_positions = []
region_num = 0
np_array_orig = copy(np_array)
np_array = np.repeat(np.repeat(np_array,3,axis=1), [3]*len(np_array), axis=0)
for i in range(0, np_array.shape[0]):
    print(f"{i} / {np_array.shape[0]}")
    for j in range(0, np_array.shape[0]):
        if (i, j) in checked_positions:
            continue

        region_positions = [(i, j)]
        while len(region_positions) > 0:
            pos = region_positions.pop()
            if pos in checked_positions:
                continue
            checked_positions.append(pos)
            region_positions_dict[region_num].append(pos)
            # print(pos)
            same_type_neighbours, fences_needed = check_neighbours(pos, np_array)
            # pos_type = np_array[(i, j)]
            # all_fences_needed[pos_type].extend(fences_needed)
            # all_fences_needed[pos_type] += len(fences_needed) # extend(fences_needed)
            # areas[pos_type] += 1
            if len(same_type_neighbours) < 4:
                regions_perimeter_squares[region_num].append(pos)
            all_fences_needed[region_num] += len(fences_needed)
            areas[region_num] += 1
            region_positions.extend(same_type_neighbours)

        region_num += 1

total_price = 0
for region in all_fences_needed:
    price = all_fences_needed[region] * areas[region]
    total_price += price

print(total_price)

def rotate_45_degrees(direction):
    if direction == (-1, 0):
        new_direction = (-1, 1)
    elif direction == (-1, 1):
        new_direction = (0, 1)
    elif direction == (0, 1):
        new_direction = (1, 1)
    elif direction == (1, 1):
        new_direction = (1, 0)
    elif direction == (1, 0):
        new_direction = (1, -1)
    elif direction == (1, -1):
        new_direction = (0, -1)
    elif direction == (0, -1):
        new_direction = (-1, -1)
    # elif direction == (-1, -1):
    #     new_direction = (-1, 0)
    else:
        new_direction = (-1, 0)
    return new_direction


def rotate_90_degrees(direction):
    if direction == (-1, 0):
        new_direction = (0, 1)
    elif direction == (0, 1):
        new_direction = (1, 0)
    elif direction == (1, 0):
        new_direction = (0, -1)
    else:
        new_direction = (-1, 0)
    return new_direction


def rotate_90_degrees_anticlockwise(direction):
    if direction == (0, 1):
        new_direction = (-1, 0)
    elif direction == (1, 0):
        new_direction = (0, 1)
    elif direction == (0, -1):
        new_direction = (1, 0)
    else:
        new_direction = (0, -1)
    return new_direction


def take_step(position, direction):
    # position = (pos_and_dir[0], pos_and_dir[1])
    # direction = (pos_and_dir[2], pos_and_dir[3])
    # return (position[0] + direction[0], position[1] + direction[1],
    #         direction[0], direction[1])
    return (position[0] + direction[0], position[1] + direction[1])


# def walk_perimeter(positions):
#     initial_pos = sorted(positions)[0]
#     direction = (0, 1)
#
#     initial_pos_and_dir = (initial_pos[0], initial_pos[1], direction[0], direction[1])
#     edges = 0
#
#
#     # if take_step(initial_pos_and_dir) not in positions:
#     #     direction = rotate_90_degrees(direction)
#     #     edges += 1
#     #     pos_and_dir = (initial_pos[0], initial_pos[1], direction[0], direction[1])
#     # else:
#     #     pos = take_step(initial_pos_and_dir)
#     #     pos_and_dir = (pos[0], pos[1], direction[0], direction[1])
#
#     pos_and_dir = None
#     visited_positions_and_directions = []
#     while pos_and_dir != initial_pos_and_dir:
#         if pos_and_dir is None:
#             pos_and_dir = initial_pos_and_dir
#         next_step = take_step(pos_and_dir)
#         if (next_step[0], next_step[1]) not in positions or next_step in visited_positions_and_directions:
#             direction = rotate_90_degrees((pos_and_dir[2], pos_and_dir[3]))
#             pos_and_dir = (pos_and_dir[0], pos_and_dir[1], direction[0], direction[1])
#             edges += 1
#         else:
#             pos_and_dir = (next_step[0], next_step[1], 0, 1)
#             visited_positions_and_directions.append(pos_and_dir)
#         print(pos_and_dir)
#
#     return edges


def walk_perimeter(perimeter_positions, all_positions):
    initial_pos = sorted(perimeter_positions)[0]
    direction = (0, 1)

    # initial_pos_and_dir = (initial_pos[0], initial_pos[1], direction[0], direction[1])
    edges = 0
    # if take_step(initial_pos_and_dir) not in positions:
    #     direction = rotate_90_degrees(direction)
    #     edges += 1
    #     pos_and_dir = (initial_pos[0], initial_pos[1], direction[0], direction[1])
    # else:
    #     pos = take_step(initial_pos_and_dir)
    #     pos_and_dir = (pos[0], pos[1], direction[0], direction[1])

    pos = None
    visited_positions = []
    while pos != initial_pos:
        if pos is None:
            pos = initial_pos
        # direction = (0, 1)

        # if direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        #     direction = rotate_45_degrees(direction)

        # print(pos)
        # Always try to turn left
        previous_direction = direction
        direction = rotate_90_degrees_anticlockwise(previous_direction)
        next_step = take_step(pos, direction)
        if next_step == initial_pos:
            pos = initial_pos
            visited_positions.append(pos)
            edges += 1
            break
        if (next_step in perimeter_positions) and (next_step not in visited_positions):
            pos = take_step(pos, direction)
            edges += 1
            visited_positions.append(pos)
            continue
        # elif (next_step in all_positions) and (next_step not in visited_positions):
        #     pos = take_step(pos, direction)
        #     edges += 1
        #     visited_positions.append(pos)
        #     continue

        # Then try continuing straight
        direction = previous_direction
        next_step = take_step(pos, direction)
        if next_step == initial_pos:
            pos = initial_pos
            visited_positions.append(pos)
            edges += 1
            break
        if (next_step in perimeter_positions) and (next_step not in visited_positions):
            pos = take_step(pos, direction)
            visited_positions.append(pos)
            continue

        # Then try changing direction
        directions_tried = 0
        while (next_step not in perimeter_positions) or (next_step in visited_positions):
        # if next_step not in positions:# or next_step in visited_positions_and_directions:
            direction = rotate_90_degrees(direction)
            next_step = take_step(pos, direction)
            directions_tried += 1
            if directions_tried == 4:
                break

        if (next_step in perimeter_positions) and (next_step not in visited_positions):
            pos = take_step(pos, direction)
            edges += 1
        elif (next_step in all_positions) and (next_step not in visited_positions):
            pos = next_step

        while (next_step not in all_positions) or (next_step in visited_positions):
        # if next_step not in positions:# or next_step in visited_positions_and_directions:
            direction = rotate_90_degrees(direction)
            next_step = take_step(pos, direction)
            # directions_tried += 1
            pos = next_step


        # Then try changing direction
        # directions_tried = 0
        # while (next_step not in all_positions) or (next_step in visited_positions):
        # # if next_step not in positions:# or next_step in visited_positions_and_directions:
        #     direction = rotate_90_degrees(direction)
        #     next_step = take_step(pos, direction)
        #     directions_tried += 1
        #     if directions_tried == 4:
        #         break

        # while (next_step not in perimeter_positions) or (next_step in visited_positions):
        # # if next_step not in positions:# or next_step in visited_positions_and_directions:
        #     direction = rotate_45_degrees(direction)
        #     next_step = take_step(pos, direction)
        #     # pos_and_dir = (pos_and_dir[0], pos_and_dir[1], direction[0], direction[1])

        visited_positions.append(pos)

    return visited_positions, edges

total_price = 0
for region_num in regions_perimeter_squares:
    print(region_num / len(regions_perimeter_squares))
    visited_positions = []
    edges_count = 0
    region_perimeter_squares = regions_perimeter_squares[region_num]
    # print('hi')
    region_all_squares = region_positions_dict[region_num]
    while len(region_perimeter_squares) > 0:
        visited_squares, edges = walk_perimeter(region_perimeter_squares, region_all_squares)
        edges_count += edges
        region_perimeter_squares = [i for i in region_perimeter_squares if i not in visited_squares]
        # region_all_squares = [i for i in region_all_squares if i not in visited_squares]
    # print(region_num, edges_count)
    print(edges_count, areas[region_num] // 9, edges_count * areas[region_num] // 9)
    total_price += edges_count * areas[region_num] // 9
    # print(total_price)


# def add_in_missing_corners(perimeter_positions, all_positions):
#     for pos in perimeter_positions:
#         print(pos)
#         for i in [-1, 1]:
#             for j in [-1, 1]:
#                 if (pos[0] + i, pos[1] + j) in perimeter_positions:
#                     if (pos[0], pos[1] + j) not in perimeter_positions or (pos[0] + i, j) not in perimeter_positions:
#                         print(pos, i, j)
#                         print((pos[0], pos[1] + j), (pos[0], pos[1] + j) in all_positions)
#                         print((pos[0] + i, j), (pos[0] + i, j) in all_positions)

print(total_price)

import numpy as np

# with open('day04_test_input.txt') as f:
with open('day04_input.txt') as f:
    data = f.read()

lines = data.split('\n')
dataarray = []
for line in lines:
    dataarray.append([i for i in line])
np_array = np.array(dataarray)

# Find Xs
m_values = np.column_stack(np.where(np_array == 'M'))
m_values = [tuple(i) for i in m_values]

def check_neighbours(array, pos, target='A'):
    # possible_dirs = [[-1, -1], [-1, 0], [-1, 1],
    #                  [0, -1],  [0, 1],
    #                  [1, -1], [1, 0], [1, 1]]
    # Purley horizontal or vertical moves aren't relevant anymore
    possible_dirs = [[-1, -1], [-1, 1],
                      [1, -1], [1, 1]]
    matching_mas_end_positions = []
    for possible_dir in possible_dirs:
        pos_to_check = tuple(np.array(pos) + np.array(possible_dir))
        if pos_to_check[0] < 0 or pos_to_check[0] >= array.shape[0]:
            continue
        elif pos_to_check[1] < 0 or pos_to_check[1] >= array.shape[1]:
            continue

        if array[pos_to_check] != target:
            continue

        # Two letters in a row - now need to keep going in same direction and check for remaining
        # letters
        next_pos_to_check = tuple(np.array(pos_to_check) + np.array(possible_dir))
        if next_pos_to_check[0] < 0 or next_pos_to_check[0] >= array.shape[0]:
            continue
        elif next_pos_to_check[1] < 0 or next_pos_to_check[1] >= array.shape[1]:
            continue
        if array[next_pos_to_check] != 'S':
            continue

        print(f"Match found starting at {pos} and going in direction {possible_dir}")

        top_position = min([pos, pos_to_check, next_pos_to_check])
        bottom_position = max([pos, pos_to_check, next_pos_to_check])
        matching_mas_end_positions.append([top_position, bottom_position])
    return matching_mas_end_positions

mas_position_ends = []
for m in m_values:
    check_neighbours_output = check_neighbours(np_array, m)
    if check_neighbours_output:
        mas_position_ends.extend(check_neighbours_output)

"""
mas_positions is a list of pairs of tuples defining start and end positions of MAS appearances, e.g
[(0, 1), (2, 3],
[(1, 5), (3, 7)],

For a X-MAS match, we need to have two MASs, a and b, like:

....a.b...
.....X....
....b.a...

Example: a = [(0, 11), (2, 9)]
         b = [(0, 9),  (2, 11)]
         
There's a crossing where two of the coordinates are the same and the other two are flipped
"""

x_mas_match_count = 0
for i in mas_position_ends:
    for j in mas_position_ends:
        if i == j:
            continue

        # For a cross,
        if ((i[0][0] == j[0][0]) and (i[1][0] == j[1][0])
                and (i[0][1] == j[1][1]) and (i[1][1] == j[0][1])):
            x_mas_match_count += 1
            print(f"{i} and {j} cross")
            continue

# We'll double count, so divide by two for the answer
print(x_mas_match_count / 2)

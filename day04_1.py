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
x_values = np.column_stack(np.where(np_array == 'X'))
x_values = [tuple(i) for i in x_values]

def check_neighbours(array, pos, target='M'):
    possible_dirs = [[-1, -1], [-1, 0], [-1, 1],
                     [0, -1],  [0, 1],
                     [1, -1], [1, 0], [1, 1]]
    match_count = 0
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
        if array[next_pos_to_check] != 'A':
            continue

        next_pos_to_check = tuple(np.array(next_pos_to_check) + np.array(possible_dir))
        if next_pos_to_check[0] < 0 or next_pos_to_check[0] >= array.shape[0]:
            continue
        elif next_pos_to_check[1] < 0 or next_pos_to_check[1] >= array.shape[1]:
            continue
        if array[next_pos_to_check] != 'S':
            continue

        print(f"Match found starting at {pos} and going in direction {possible_dir}")
        match_count += 1

    return match_count

overall_match_count = 0
for x in x_values:
    overall_match_count += check_neighbours(np_array, x)

print(overall_match_count)
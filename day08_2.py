import numpy as np

# with open('day08_test_input.txt') as f:
with open('day08_input.txt') as f:
    data = f.read()

lines = data.strip('\n').split('\n')
dataarray = []
for line in lines:
    dataarray.append([i for i in line])
np_array = np.array(dataarray)

antenna_frequencies = [i for i in np.unique(np_array) if i != '.']

def find_antinodes(np_array, freq):
    x, y = np.where(np_array == freq)
    antenna_coords = [(i, j) for i, j in zip(x, y)]

    antinode_coords = []
    for antenna_a in antenna_coords:
        for antenna_b in antenna_coords:
            if antenna_a == antenna_b:
                continue

            a_to_b = (antenna_b[0] - antenna_a[0], antenna_b[1] - antenna_a[1])

            gradient = a_to_b[1] / a_to_b[0]
            intercept = antenna_a[1] - gradient * antenna_a[0]

            for x in range(0, np_array.shape[0]):
                y = gradient * x + intercept

                if y <= -1:
                    continue

                # Only consider integer values of y
                if round(y, 6) % 1 != 0:  # Rounding so we don't leave out values like 3.00000001
                    # print(f"skipping {y}")
                    continue

                # Round off values as ints so the call to set(all_antinode_coords)) below drops
                # duplicates correctly
                antinode_coord = (int(round(x, 0)), int(round(y, 0)))
                if antinode_coord[0] < 0 or antinode_coord[0] >= np_array.shape[0]:
                    continue
                if antinode_coord[1] < 0 or antinode_coord[1] >= np_array.shape[1]:
                    continue

                antinode_coords.append(antinode_coord)
    return antinode_coords


all_antinode_coords = []
for freq in antenna_frequencies:
    all_antinode_coords.extend(find_antinodes(np_array, freq))

print(len(set(all_antinode_coords)))
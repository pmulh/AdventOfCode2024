import pandas as pd

# input = pd.read_csv('day01-1_test_input.csv', header=None, delimiter='   ')
input = pd.read_csv('day01-1_input.csv', header=None, delimiter='   ',)

list_1 = input[0].sort_values().reset_index(drop=True)
list_2 = input[1].sort_values().reset_index(drop=True)

both_lists = pd.concat([list_1, list_2], ignore_index=True, axis=1)
both_lists['diff'] = abs(both_lists[0] - both_lists[1])
print(both_lists['diff'].sum())


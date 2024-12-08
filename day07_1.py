from itertools import product

# with open('day07_test_input.txt') as f:
with open('day07_input.txt') as f:
    data = f.read()

lines = data.strip('\n').split('\n')

targets_sum = 0
for line in lines:
    target, values = line.split(': ')
    target = int(target)
    values = [int(i) for i in values.split(' ')]
    operators = [['+', '*'] for i in range(len(values) - 1)]

    # Make all possible combinations of operators
    possible_operator_lists = list(product(*operators))
    for operator_list in possible_operator_lists:
        result = values[0]
        for i in range(1, len(values)):
            if operator_list[i-1] == '+':
                result += values[i]
            else:
                result *= values[i]

        if result == target:
            targets_sum += target
            break

print(targets_sum)


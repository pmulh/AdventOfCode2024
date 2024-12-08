from itertools import product

# with open('day07_test_input.txt') as f:
with open('day07_input.txt') as f:
    data = f.read()

lines = data.strip('\n').split('\n')

def check_sum(line, valid_operators):
    target, values = line.split(': ')
    target = int(target)
    values = [int(i) for i in values.split(' ')]
    operators = [valid_operators for i in range(len(values) - 1)]

    # Make all possible combinations of operators
    possible_operator_lists = list(product(*operators))
    for operator_list in possible_operator_lists:
        result = values[0]
        for i in range(1, len(values)):
            if operator_list[i-1] == '+':
                result += values[i]
            elif operator_list[i-1] == '*':
                result *= values[i]
            else:
                result = int(str(result) + str(values[i]))

        if result == target:
            return True, target

    return False, line


targets_sum = 0
# Remove as a many as we can from the two operator checks
remaining_lines = []
for line in lines:
    success, output = check_sum(line, valid_operators=['+', '*'])
    if success:
        # print(line)
        targets_sum += output
    else:
        remaining_lines.append(line)

print(targets_sum)

# Check remaining lines using three operator checks
for line in remaining_lines:
    success, output = check_sum(line, valid_operators=['+', '*', '||'])
    if success:
        targets_sum += output

print(targets_sum)
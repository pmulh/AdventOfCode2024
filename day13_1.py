# with open('day13_test_input.txt') as f:
with open('day13_input.txt') as f:
        data = f.read()

def find_possible_winning_combos(machine_info):
    x_a = machine_info['x_a']
    y_a = machine_info['y_a']
    x_b = machine_info['x_b']
    y_b = machine_info['y_b']
    target_x = machine_info['target_x']
    target_y = machine_info['target_y']
    possible_button_press_combinations = []
    for a_presses in range(0, 101):
        b_presses = (target_x - x_a * a_presses) / x_b
        # print(b_presses, b_presses % 1)
        if b_presses % 1 != 0:
            continue
        if b_presses < 0:
            continue
        if b_presses > 100:
            continue

        if (a_presses * x_a) + (b_presses * x_b) != target_x:
            continue
        if (a_presses * y_a) + (b_presses * y_b) != target_y:
            continue

        possible_button_press_combinations.append((a_presses, int(b_presses)))
    return possible_button_press_combinations


def find_lowest_cost_combination(possible_button_press_combinations):
    a_press_cost = 3
    b_press_cost = 1
    lowest_cost = -1
    cheapest_combination = None
    for combo in possible_button_press_combinations:
        cost = combo[0] * a_press_cost + combo[1] * b_press_cost
        if lowest_cost == -1 or cost < lowest_cost:
            lowest_cost = cost
            cheapest_combination = combo

    return cheapest_combination, lowest_cost


lines = data.strip('\n').split('\n')

machines = {}
machine_number = 0
machines[machine_number] = {}
for line in lines:
    if line == '':
        machine_number += 1
        machines[machine_number] = {}
        continue
    if 'Button A' in line:
        x_a = int(line.split('X+')[1].split(',')[0])
        y_a = int(line.split('Y+')[1])
        machines[machine_number]['x_a'] = x_a
        machines[machine_number]['y_a'] = y_a
    if 'Button B' in line:
        x_b = int(line.split('X+')[1].split(',')[0])
        y_b = int(line.split('Y+')[1])
        machines[machine_number]['x_b'] = x_b
        machines[machine_number]['y_b'] = y_b
    if 'Prize' in line:
        target_x = int(line.split('X=')[1].split(',')[0])
        target_y = int(line.split('Y=')[1])
        machines[machine_number]['target_x'] = target_x
        machines[machine_number]['target_y'] = target_y


print('hi')
total_cost = 0
winnable_machines = 0
for machine_number in machines:
    possible_winning_combos = find_possible_winning_combos(machines[machine_number])
    if len(possible_winning_combos) == 0:
        print(f"{machine_number=} can't be won")
        continue
    cheapest_combo, lowest_cost = find_lowest_cost_combination(possible_winning_combos)
    print(machine_number, cheapest_combo, lowest_cost)
    total_cost += lowest_cost
    winnable_machines += 1

print(winnable_machines)
print(total_cost)
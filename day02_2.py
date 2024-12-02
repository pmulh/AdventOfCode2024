from collections import Counter


def are_levels_safe(levels):
    if levels[1] > levels[0]:
        mode = 'increasing'
    else:
        mode = 'decreasing'

    i = 1
    category = 'safe'
    while category == 'safe' and i < len(levels):
        if levels[i] >= levels[i-1] and mode == 'decreasing':
            category = 'unsafe'
        if levels[i] <= levels[i-1] and mode == 'increasing':
            category = 'unsafe'
        if mode == 'decreasing' and levels[i-1] - levels[i] > 3:
            category = 'unsafe'
        if mode == 'increasing' and levels[i] - levels[i-1] > 3:
            category = 'unsafe'
        i += 1
    if category == 'safe':
        return True


def can_levels_be_made_safe(levels):
    # If there's two or more duplicate numbers, removing one can't make it safe
    if Counter(levels).most_common(2)[1][1] > 1:
        return False

    for i in range(0, len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if new_levels == sorted(new_levels) or new_levels == sorted(new_levels, reverse=True):
            # Only return True if we have no duplicates after removing an element, and if the gaps
            # between consecutive numbers is <= 3
            if ((Counter(new_levels).most_common(1)[0][1] == 1)
                    and (max([abs(new_levels[i+1] - new_levels[i]) for i in range(0, len(levels)-2)]) <= 3)):
                return True

    return False


# with open('day02-1_test_input.txt') as f:
with open('day02-1_input.txt') as f:
        data = f.read()

lines = data.split('\n')

safe_lines = 0
for line in lines:
    if not line:
        continue

    levels = [int(i) for i in line.split(' ')]

    if are_levels_safe(levels):
        print(f"{levels} --> safe already")
        safe_lines += 1
    elif can_levels_be_made_safe(levels):
        print(f"{levels} --> can be made safe")
        safe_lines += 1
    else:
        print(f"{levels} --> can't be made safe")

print(safe_lines)

with open('day01-1_test_input.txt') as f:
# with open('day01-1_input.txt') as f:
        data = f.read()

lines = data.split('\n')

safe_lines = 0
for line in lines:
    if not line:
        continue
    category = 'safe'
    levels = [int(i) for i in line.split(' ')]
    if levels[1] > levels[0]:
        mode = 'increasing'
    else:
        mode = 'decreasing'

    i = 1
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
        safe_lines += 1

print(safe_lines)
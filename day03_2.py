import re

# with open('day03_test_input.txt') as f:
# with open('day03_2_test_input.txt') as f:
with open('day03_input.txt') as f:
    data = f.read()

sum = 0
data_split = data.split('mul')
for j in range(len(data_split)):
    i = data_split[j]

    most_recent_do_pos = -1
    most_recent_dont_pos = -1

    preceding_characters = ''.join(data_split[:j])

    # Find the most recent "do"" (making sure to not match on don't)
    # do_matches = [i.start() for i in re.finditer(r'(?<!g)do(?!n\'t)', preceding_characters)]
    # Actually, regex can be simpler
    do_matches = [i.start() for i in re.finditer(r'do(?!n\'t)', preceding_characters)]
    if do_matches:
        most_recent_do_pos = do_matches[-1]

    # Find the most recent "don't"
    dont_matches = [i.start() for i in re.finditer(r'don\'t', preceding_characters)]
    if dont_matches:
        most_recent_dont_pos = dont_matches[-1]

    # If "don't" has appeared more recently than "do", don't add to sum
    if most_recent_dont_pos > most_recent_do_pos:
        continue

    # Get characters between brackets
    if i.find('(') != 0 or i.find(')') <= i.find('('):
        continue
    chars_in_brackets = i[i.find('(') + 1:i.find(')')].split(',')
    if len(chars_in_brackets) != 2:
        continue
    try:
        sum += int(chars_in_brackets[0]) * int(chars_in_brackets[1])
        # print(f'Adding {chars_in_brackets}')
        print(f'Adding {i}')
    except:
        continue

print(sum)

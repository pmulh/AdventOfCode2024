# with open('day03_test_input.txt') as f:
with open('day03_input.txt') as f:
    data = f.read()

sum = 0
for i in data.split('mul'):
    # Skip anything that doesn't start with a ( and have a ) in it somewhere
    if i.find('(') != 0 or i.find(')') <= i.find('('):
        continue
    # Get characters between brackets
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

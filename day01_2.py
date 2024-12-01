import pandas as pd

# input = pd.read_csv('day01-1_test_input.csv', header=None, delimiter='   ', engine='python')
input = pd.read_csv('day01-1_input.csv', header=None, delimiter='   ', engine='python')

# list_1_value_counts = input[0].value_counts().to_dict()  # Dont' actually need this
list_2_value_counts = input[1].value_counts().to_dict()

similarity_score = (
    input[0]
    .apply(lambda x: 0 if x not in list_2_value_counts else x * list_2_value_counts[x])
    .sum()
)

print(similarity_score)



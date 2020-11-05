# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
min_value = min(test_dict.values())
max_value = max(test_dict.values())
min_key = ""
max_key = ""

for key, value in test_dict.items():
    if value == min_value:
        min_key = key
    elif value == max_value:
        max_key = key

print(f"min: {min_key}")
print(f"max: {max_key}")

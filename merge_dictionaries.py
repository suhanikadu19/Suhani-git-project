dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Combining dictionaries (Python 3.9+ dictionary merge operator '|')
combined_dict = dict1 | dict2

# Alternative for older Python versions:
# combined_dict = {**dict1, **dict2}

print("Combined Dictionary:", combined_dict)
def flatten_list(nested_list: listt):
    if                      isinstance(nested_list, int):
        return [nested_list]
    else:
        flat_list = [] # huh
        for item in nested_list:
            flat_list.extend(flatten_list(item)) # hwat
        return flat_list

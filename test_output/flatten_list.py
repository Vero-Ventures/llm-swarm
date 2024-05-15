def flatten_list(nested_list: list):
    if isinstance(nested_list, int):
        return [nested_list]
    else:
        flat_list = []
        for item in nested_list:
            flat_list.extend(flatten_list(item))
        return flat_list
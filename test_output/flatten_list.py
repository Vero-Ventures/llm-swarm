def flatten_list(nested_list: list):
    """
    Flattens a nested list into a single list.

    Args:
        nested_list (list): A list that may contain nested lists.

    Returns:
        list: A flattened list containing all the elements from the original list.
    """
    if isinstance(nested_list, int):
        return [nested_list]
    else:
        flat_list = []
        for item in nested_list:
            flat_list.extend(flatten_list(item))
        return flat_list
def clean_python_code(result: str) -> str:
    """
    Cleans up the result string by removing non-Python code markers and any text
    following the Python code block.

    Args:
        result (str): The string containing potentially marked-up Python code.

    Returns:
        str: The cleaned Python code.
    """
    # Find the start of the Python code block
    start_idx = result.find('```python')
    if start_idx != -1:
        # Adjust start index to skip the marker
        start_idx += len('```python')
    else:
        # If no start marker, start from the beginning of the string
        start_idx = 0

    # Find the end of the Python code block
    end_idx = result.find('```', start_idx)
    if end_idx == -1:
        # If no end marker, end at the last character of the string
        end_idx = len(result)

    # Extract the Python code
    python_code = result[start_idx:end_idx].strip()

    # Return the clean Python code
    return python_code
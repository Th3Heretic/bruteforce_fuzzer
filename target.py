def vulnerable_function(input_data):
    """
    A dummy vulnerable function.
    Replace this logic with the actual target you wish to test.
    """
    # For demonstration: trigger vulnerability if the input matches a specific string.
    if input_data == "exploit":
        raise Exception("Vulnerability triggered!")
    # Simulate normal processing
    return input_data.upper()
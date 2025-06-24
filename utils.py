def validate_integer_list(input_list):
    try:
        return [int(i) for i in input_list]
    except ValueError:
        raise ValueError("List must contain only integers.")

def validate_string_list(input_list):
    if not all(isinstance(s, str) for s in input_list):
        raise ValueError("List must contain only strings.")
    return input_list

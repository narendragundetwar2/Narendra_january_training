def save_error_fixed(error, errors=None):
    if errors is None:
        errors = []
    errors.append(error)
    return errors
print(save_error_fixed("E1"))
print(save_error_fixed("E2"))
print(save_error_fixed("E3"))

Output- ['E1']
        ['E2']
        ['E3']  
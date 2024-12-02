def calculate_structure_sum(*data_structure):
    summ_ = 0
    for _ in data_structure:
        if isinstance(_, int):
            summ_ += _
        elif isinstance(_, str):
            summ_ += len(_)
        elif isinstance(_,(list, set, tuple)):
            summ_ += calculate_structure_sum(*_)
        elif isinstance(_,dict):
            summ_ += calculate_structure_sum(*_.items())
    return summ_
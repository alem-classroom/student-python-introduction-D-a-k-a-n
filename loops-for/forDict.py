def reverse_dict(dict):
    # swap keys and values within dict and return dict
    x = dict.keys()
    res = {}
    for i in list(x):
        res[dict[i]] = i

    return res

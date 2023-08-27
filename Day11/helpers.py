from more_itertools import first


def generate_next_char_map(chars, illegal_chars):
    next_char_map = {}
    val_chars = chars[1:] + chars[0]
    for ind, key in enumerate(chars):
        # prevent mapping to illegal chars
        valid_vals = filter(lambda c: c not in illegal_chars, val_chars[ind:])
        next_char_map[key] = first(valid_vals)
    return next_char_map

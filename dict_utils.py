def merge(a_dict, key, value, merging_func):
    """
        Merge a value in a dict.

        * if `key` is not in `a_dict`, then performs
          a_dict[key] = value
        * if `key` is already in `a_dict`, then performs:
          a_dict[key] = merging_func(a_dict[key], an_array)
    """
    if key not in a_dict:
        a_dict[key] = value
    else:
        a_dict[key] = merging_func(a_dict[key], value)


def matching(a_dict, substr):
    """
        Returns the items of the string-key dictionary `a_dict`
        which keys matches all the substrings in `substr`.
    """

    items = []
    if not isinstance(substr, list):
        substr = [substr]
    for k in a_dict:
        if sum([k.find(s) >= 0 for s in substr]) == len(substr):
            items.append((k, a_dict[k]))
    return items


def matching_uniq(a_dict, substr):
    """
        Returns, if it exists, the unique item
        of the string-key dictionary `a_dict`
        which keys matches all the substrings in `substr`.

        Raises an exception when none or several keys match.
    """
    items = matching(a_dict, substr)
    if len(items) == 0:
        raise KeyError('No key matches the substring.')
    if len(items) > 1:
        raise KeyError('Several keys match the substring.')

    return items[0]

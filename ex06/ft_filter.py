def ft_filter(function, iterable):
    (
        "filter(function or None, iterable) --> filter object\n\n"
        "Return an iterator yielding those items of iterable for which "
        "function(item)\nis true. If function is None, return the items "
        "that are true."
    )
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]

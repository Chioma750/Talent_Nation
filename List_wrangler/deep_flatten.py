def deep_flatten(items):
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)

    return result
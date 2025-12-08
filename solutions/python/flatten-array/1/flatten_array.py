def flatten(iterable):
    result = []

    def walk(node):
        for item in node:
            if item == None:
                continue
            if isinstance(item,list):
                walk(item)
            else :
                result.append(item)

    walk(iterable)
    return result
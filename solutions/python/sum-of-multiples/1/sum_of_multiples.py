def sum_of_multiples(limit, multiples):
    combine_set = set()
    for base_item in multiples:
        if base_item <= 0:
            continue
        for p in range(base_item,limit,base_item):
            combine_set.add(p)

    return sum(combine_set)
def find(org_search_list, value):
    low = 0
    high = len(org_search_list)-1

    while low <= high:
        mid = (low + high )// 2
        if org_search_list[mid] == value:
            return mid
        elif org_search_list[mid] > value:
            high = mid - 1
        elif org_search_list[mid] < value:
            low = mid + 1

    raise ValueError("value not in array")
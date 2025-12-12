def append(list1, list2):
    if isinstance(list2, list):
        for items in list2:
            list1.append(items)
    else:
        list1.append(list2)
        
    return list1

def concat(lists):
    all_in_one_list = []
    for items in lists:
        all_in_one_list = append(all_in_one_list,items)

    return all_in_one_list

def filter(function, list):
    result = []
    for items in list:
        if function(items):
            result = append(result,items)
            
    return result

def length(list):
    length = 0
    for i in list:
        length+=1

    return length

def map(function, list):
    result = []
    for items in list:
        result = append(result,function(items))

    return result

def foldl(function, lst, initial):
    acc = initial
    for item in lst:
        acc = function(acc, item)
    return acc

def foldr(function, lst, initial):
    acc = initial
    index = len(lst) - 1
    while index >= 0:
        acc = function(acc, lst[index])   # ← correct order!
        index -= 1
    return acc

def reverse(list):
    l = len(list)-1
    result = []
    while l>=0:
        result.append(list[l])
        l-=1

    return result
        
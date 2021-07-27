def un_search(unordered_list, term):           #searching unordered list
    unordered_list_size = len(unordered_list)
    for i in range(unordered_list_size):
        if term == unordered_list[i]:
           return i
    return None

def or_search (ordered_list, term):     #searching ordered list
    ordered_list_size = len(ordered_list)
    for i in range(ordered_list_size):
        if term == ordered_list[i]:
            return i
        elif ordered_list[i] > term:
            return None            
    return None                                
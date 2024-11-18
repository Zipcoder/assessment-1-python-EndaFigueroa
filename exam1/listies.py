
def drop_last(lst):
    answer = lst
    answer.pop()
    return answer
    # """
    # This function takes a list and returns a list with the last item removed.
    # """
    # pass  # implement me

def drop_mangle(lst):
    answer = lst[2:-1]
    return answer
    # """
    # This function takes a list and returns a list with the first two items AND last item removed.
    # """
    # pass  # implement me

def add_item_front(lst, a):
    answer = lst
    answer.insert(0,a)
    return answer
    # """
    # This function takes a list and an item,
    # returning the list with the item prepended to the list
    # """
    # pass  # implement me

def add_item_end(lst, a):
    answer = lst
    answer.append(a)
    return answer
    # """
    # This function takes a list and an item,
    # returning the list with the item appended to the list
    # """
    # pass  # implement me

def drop_first_two(lst):
    answer = lst[2:]
    return answer
    # """
    # This function takes a list and returns a list with the first two items removed.
    # """
    # pass  # implement me

def drop_last_two(lst):
    answer = lst[:-2]
    return answer
    
    # """
    # This function takes a list and returns a list with the last two items removed.
    # """
    # pass  # implement me


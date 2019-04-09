def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""

    if int_list is None:
        raise ValueError
    if int_list == []:
        return None
    int_max = int_list[0]
    for i in range(len(int_list)):
        if int_list[i] > int_max:
            int_max = int_list[i]
    return int_max


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if int_list == []:
        return []

    return [int_list[-1]] + reverse_rec(int_list[:-1])


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """

    center = ((high+low)//2)
    if int_list is None:
        raise ValueError
    if int_list == []:
        return None
    if int_list[center] == target:
        return center
    if int_list[center] < target:
        return bin_search(target, center+1, high, int_list)
    if int_list[center] > target:
        return bin_search(target, low, center-1, int_list)

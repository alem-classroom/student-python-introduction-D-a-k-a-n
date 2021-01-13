def size_of_list(list):
    return len(list)


def add_elem_to_list(list, elem):
    return list.append(elem)


def delete_elem_from_list(list, index = -1):
    # delete element from list, such that its index is index
    # if index is invalid, return empty list
    if index == -1:
        return list
    return list.pop(index)


def count_elements_in_list(list, x):
    # count elements in the list that are equal to x and return the coun
    return list.count(x)


def sort_list(list):
    # return sorted list
    return list.sort()


def reverse(list):
    # return reversed list
    return list.reverse()

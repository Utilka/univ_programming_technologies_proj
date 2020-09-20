def bisect(input_list, x, ascend, low=0, high=None):
    if high is None:
        high = len(input_list)

    while low < high:
        mid = (low + high) // 2
        l_m = input_list[mid]
        if (l_m < x) * ascend + (l_m > x) * (not ascend):  # expr is  l[mid]<x on ascend ,l[mid]>x on descend
            low = mid + 1
        else:
            high = mid
    return low

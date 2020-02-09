from mean import get_mean

"""
The median is the point that divides the group into two
equal parts - the upper half and the lower half.


"""


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def get_median(items=[]):
    n = len(items)
    index = 0
    items.sort()
    if is_even(n):
        middle_low = int((n / 2) - 1)
        middle_high = int(((n / 2) + 1) - 1)
        median = get_mean([items[middle_low], items[middle_high]])
        return median
    else:
        index = int(n + 1) / 2
        return items[int(index) + 1]

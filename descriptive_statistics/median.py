"""
The median is the point that divides the group into two
equal parts - the upper half and the lower half.


"""


def get_median(items=[]):
    items.sort()
    index = int((len(items)) / 2)
    return items[index]

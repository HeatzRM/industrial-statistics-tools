from mean import get_mean


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def get_median(items=[]):
    """
    The median is the point that divides the group into two
    equal parts - the upper half and the lower half.
    """
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
        return items[int(index) - 1]


def get_total_number_of_cases(items=[{}]):
    total = 0
    for item in items:
        total = total + item["freq"]
    return total


def create_cumulative_frequency(items=[{}]):
    for index, item in enumerate(items):
        if index != 0:
            item["CF"] = item["freq"] + items[index - 1]["CF"]
        else:
            item["CF"] = item["freq"]
        items[index] = item
    return items


def get_median_freq_dist(data=[{}], interval=0):
    """
    Formula for finding the median from a
    Frequency Distribution:

    median = lower_bound + (((number_of_cases/2) - cumulative_frequency) / frequency) *  interval
    """
    data = create_cumulative_frequency(data)

    number_of_cases = get_total_number_of_cases(data)

    median_class_index = get_class_index(data)

    lower_boundary = data[median_class_index]["lower"] - 0.5
    final_cumulative_frequency_index = get_final_cumulative_frequency(
        items=data, number_of_cases=number_of_cases, index=median_class_index
    )

    median = (
        lower_boundary
        + (
            (((number_of_cases / 2) - data[final_cumulative_frequency_index]["CF"]))
            / data[median_class_index]["freq"]
        )
        * interval
    )

    return median


def get_class_index(items=[{}]):
    return items.index(max(items, key=lambda item: item["freq"]))


def get_final_cumulative_frequency(items=[{}], number_of_cases=0, index=0):
    boundary = round(number_of_cases / 2)
    while index != 0:
        if items[index]["CF"] < boundary and boundary >= items[index]["CF"]:
            return index
        else:
            index = index - 1
    return None

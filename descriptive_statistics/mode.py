from collections import Counter
from mean import get_mean
from median import get_class_index


def get_mode_ungrouped(list_of_numbers):
    """
    The mode is the score that appears most number
    of times in a distribution.

    """

    counted_numbers = Counter(list_of_numbers)
    most_common = counted_numbers.most_common(3)
    try:
        if len(most_common) >= 3:
            if (
                most_common[0][1] == most_common[1][1]
                and most_common[1][1] == most_common[2][1]
            ):
                return {"mode_type": "no mode", "mode": None}

        if most_common[0][1] == most_common[1][1]:
            return {
                "mode_type": "bi-modal",
                "modes": [most_common[0][0], most_common[1][0]],
            }
        else:
            return {"mode_type": "unimodal", "mode": most_common[0][0]}
    except IndexError:
        return None


def mode_freq_dist(data=[{}], interval=0):
    mean = get_mean(items=[data[0]["lower"], data[-1]["upper"]])
    rounded_mean = round(mean)
    median_class = get_class_index(data, rounded_mean)

    Lb = mean
    d1 = data[median_class]["freq"] - data[median_class - 1]["freq"]
    d2 = data[median_class]["freq"] - data[median_class + 1]["freq"]

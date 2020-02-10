from collections import Counter


def get_mode_ungrouped(list_of_numbers):
    """
    The mode is the score that appears most number
    of times in a distribution.

    """

    counted_numbers = Counter(list_of_numbers)
    most_common = counted_numbers.most_common(3)
    if len(most_common) >= 3:
        if most_common[0][1] == most_common[1][1] and most_common[1][1] == most_common[2][1]:
            return {"mode_type": "no mode", "mode": None}

    if most_common[0][1] == most_common[1][1]:
        return {
            "mode_type": "bi-modal",
            "modes": [most_common[0][0], most_common[1][0]],
        }
    else:
        return {"mode_type": "unimodal", "mode": most_common[0][0]}

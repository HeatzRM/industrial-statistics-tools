from median import get_median


def test():
    assert get_median([5, 7, 4, 8, 15, 12, 2, 22, 18]) == 8
    assert get_median([2, 3, 5, 7, 7, 9, 15, 12, 18, 22]) == 8

from median import (
    get_median,
    get_median_freq_dist,
    create_cumulative_frequency,
    get_final_cumulative_frequency,
    get_class_index,
)


def test_median_freq_dist():
    test_data = [
        {"lower": 20, "upper": 24, "freq": 1},
        {"lower": 25, "upper": 29, "freq": 2},
        {"lower": 30, "upper": 34, "freq": 4},
        {"lower": 35, "upper": 39, "freq": 3},
        {"lower": 40, "upper": 44, "freq": 5},
        {"lower": 45, "upper": 49, "freq": 6},
        {"lower": 50, "upper": 54, "freq": 7},
        {"lower": 55, "upper": 59, "freq": 5},
        {"lower": 60, "upper": 64, "freq": 3},
        {"lower": 65, "upper": 69, "freq": 4},
        {"lower": 70, "upper": 74, "freq": 3},
        {"lower": 75, "upper": 79, "freq": 2},
    ]

    assert round(get_median_freq_dist(data=test_data, interval=5), 2) == 50.57


def test_cumulative_freq():
    test_data = [
        {"lower": 20, "upper": 24, "freq": 1},
        {"lower": 25, "upper": 29, "freq": 2},
        {"lower": 30, "upper": 34, "freq": 4},
        {"lower": 35, "upper": 39, "freq": 3},
        {"lower": 40, "upper": 44, "freq": 5},
        {"lower": 45, "upper": 49, "freq": 6},
        {"lower": 50, "upper": 54, "freq": 7},
        {"lower": 55, "upper": 59, "freq": 5},
        {"lower": 60, "upper": 64, "freq": 3},
        {"lower": 65, "upper": 69, "freq": 4},
        {"lower": 70, "upper": 74, "freq": 3},
        {"lower": 75, "upper": 79, "freq": 2},
    ]

    expected_data = [
        {"lower": 20, "upper": 24, "freq": 1, "CF": 1},
        {"lower": 25, "upper": 29, "freq": 2, "CF": 3},
        {"lower": 30, "upper": 34, "freq": 4, "CF": 7},
        {"lower": 35, "upper": 39, "freq": 3, "CF": 10},
        {"lower": 40, "upper": 44, "freq": 5, "CF": 15},
        {"lower": 45, "upper": 49, "freq": 6, "CF": 21},
        {"lower": 50, "upper": 54, "freq": 7, "CF": 28},
        {"lower": 55, "upper": 59, "freq": 5, "CF": 33},
        {"lower": 60, "upper": 64, "freq": 3, "CF": 36},
        {"lower": 65, "upper": 69, "freq": 4, "CF": 40},
        {"lower": 70, "upper": 74, "freq": 3, "CF": 43},
        {"lower": 75, "upper": 79, "freq": 2, "CF": 45},
    ]

    assert create_cumulative_frequency(test_data) == expected_data


def test_get_final_cumulative_frequency():
    test_data = [
        {"lower": 20, "upper": 24, "freq": 1, "CF": 1},
        {"lower": 25, "upper": 29, "freq": 2, "CF": 3},
        {"lower": 30, "upper": 34, "freq": 4, "CF": 7},
        {"lower": 35, "upper": 39, "freq": 3, "CF": 10},
        {"lower": 40, "upper": 44, "freq": 5, "CF": 15},
        {"lower": 45, "upper": 49, "freq": 6, "CF": 21},
        {"lower": 50, "upper": 54, "freq": 7, "CF": 28},
        {"lower": 55, "upper": 59, "freq": 5, "CF": 33},
        {"lower": 60, "upper": 64, "freq": 3, "CF": 36},
        {"lower": 65, "upper": 69, "freq": 4, "CF": 40},
        {"lower": 70, "upper": 74, "freq": 3, "CF": 43},
        {"lower": 75, "upper": 79, "freq": 2, "CF": 45},
    ]

    assert (
        get_final_cumulative_frequency(items=test_data, number_of_cases=45, index=6)
        == 5
    )


def test_get_class_index():
    test_data = [
        {"lower": 20, "upper": 24, "freq": 1, "CF": 1},
        {"lower": 25, "upper": 29, "freq": 2, "CF": 3},
        {"lower": 30, "upper": 34, "freq": 4, "CF": 7},
        {"lower": 35, "upper": 39, "freq": 3, "CF": 10},
        {"lower": 40, "upper": 44, "freq": 5, "CF": 15},
        {"lower": 45, "upper": 49, "freq": 6, "CF": 21},
        {"lower": 50, "upper": 54, "freq": 7, "CF": 28},
        {"lower": 55, "upper": 59, "freq": 5, "CF": 33},
        {"lower": 60, "upper": 64, "freq": 3, "CF": 36},
        {"lower": 65, "upper": 69, "freq": 4, "CF": 40},
        {"lower": 70, "upper": 74, "freq": 3, "CF": 43},
        {"lower": 75, "upper": 79, "freq": 2, "CF": 45},
    ]

    assert get_class_index(test_data) == 6


def basic_test():
    assert get_median([5, 7, 4, 8, 15, 12, 2, 22, 18]) == 8
    assert get_median([2, 3, 5, 7, 7, 9, 15, 12, 18, 22]) == 8


def test():
    basic_test()
    test_cumulative_freq()
    test_get_class_index()
    test_get_final_cumulative_frequency()
    test_median_freq_dist()

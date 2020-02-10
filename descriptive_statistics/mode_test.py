from mode import get_mode_ungrouped, mode_freq_dist


def test_freq_dist():
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

    assert round(mode_freq_dist(test_data, 5), 2) == 51.17


def test():
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 1, 1, 1]
    test_data_2 = [1, 1, 1, 2, 2, 2, 3, 4, 5, 6]
    test_data_3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    test_data_4 = [2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 7, 7, 8]

    test_data_5 = []

    assert get_mode_ungrouped(test_data) == {"mode_type": "unimodal", "mode": 1}
    assert get_mode_ungrouped(test_data_2) == {"mode_type": "bi-modal", "modes": [1, 2]}
    assert get_mode_ungrouped(test_data_3) == {"mode_type": "no mode", "mode": None}
    assert get_mode_ungrouped(test_data_4) == {"mode_type": "unimodal", "mode": 5}
    assert get_mode_ungrouped(test_data_5) == None

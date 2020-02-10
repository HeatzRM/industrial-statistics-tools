from mode import get_mode_ungrouped


def test():
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 1, 1, 1]
    test_data_2 = [1, 1, 1, 2, 2, 2, 3, 4, 5, 6]
    test_data_3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

    assert get_mode_ungrouped(test_data) == {"mode_type": "unimodal", "mode": 1}
    assert get_mode_ungrouped(test_data_2) == {"mode_type": "bi-modal", "modes": [1, 2]}
    assert get_mode_ungrouped(test_data_3) == {"mode_type": "no mode", "mode": None}

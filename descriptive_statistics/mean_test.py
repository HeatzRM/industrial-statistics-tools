from mean import get_mean, get_weighted_mean


def basic_mean_test():
    assert get_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
    assert get_mean([1, 2, 3, 4, 5]) == 3.0


def basic_weighted_mean_test():
    assert (
        get_weighted_mean(
            [
                {"score": 3, "freq": 4},
                {"score": 4, "freq": 2},
                {"score": 5, "freq": 5},
                {"score": 6, "freq": 6},
                {"score": 7, "freq": 3},
            ]
        )
        == 5.1
    )

    assert (
        round(
            get_weighted_mean(
                [
                    {"score": 5, "freq": 12},
                    {"score": 4, "freq": 16},
                    {"score": 3, "freq": 2},
                    {"score": 2, "freq": 0},
                    {"score": 1, "freq": 0},
                ]
            ),
            2,
        )
        == 4.33
    )


def four_machines_efficiency_test():
    """
    - Score refers to the rating from a evaluator of a machine
    - Frequency refers to the number of times it was
        given by an employee
    """

    machine_A_data = [
        {"score": 5, "freq": 12},
        {"score": 4, "freq": 16},
        {"score": 3, "freq": 2},
        {"score": 2, "freq": 0},
        {"score": 1, "freq": 0},
    ]

    machine_B_data = [
        {"score": 5, "freq": 17},
        {"score": 4, "freq": 12},
        {"score": 3, "freq": 1},
        {"score": 2, "freq": 0},
        {"score": 1, "freq": 0},
    ]

    machine_C_data = [
        {"score": 5, "freq": 6},
        {"score": 4, "freq": 7},
        {"score": 3, "freq": 15},
        {"score": 2, "freq": 2},
        {"score": 1, "freq": 0},
    ]

    machine_D_data = [
        {"score": 5, "freq": 6},
        {"score": 4, "freq": 5},
        {"score": 3, "freq": 12},
        {"score": 2, "freq": 6},
        {"score": 1, "freq": 1},
    ]

    assert round(get_weighted_mean(machine_A_data), 2) == 4.33
    assert round(get_weighted_mean(machine_B_data), 2) == 4.53
    assert round(get_weighted_mean(machine_C_data), 2) == 3.57
    assert round(get_weighted_mean(machine_D_data), 2) == 3.30


def test():
    basic_mean_test()
    basic_weighted_mean_test()
    four_machines_efficiency_test()

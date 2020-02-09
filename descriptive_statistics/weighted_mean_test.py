from weighted_mean import get_weighted_mean


def test():
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

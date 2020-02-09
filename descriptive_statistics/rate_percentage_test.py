from rate_percentage import get_percentage


def test():
    assert round(get_percentage(frequency=86, total_number_of_cases=200), 1) == 43
    assert round(get_percentage(frequency=114, total_number_of_cases=200), 1) == 57
    assert round(get_percentage(frequency=200, total_number_of_cases=200), 1) == 100

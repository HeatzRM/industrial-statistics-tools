from determining_sample_size import determine_sample_size


def test():
    assert round(determine_sample_size(200, 0.05), 2) == 133.33
    assert round(determine_sample_size(500, 0.05), 2) == 222.22
    assert round(determine_sample_size(1200, 0.01), 2) == 1071.43
    assert round(determine_sample_size(5000, 0.05), 2) == 370.37
    assert round(determine_sample_size(2000, 0.01), 2) == 1666.67

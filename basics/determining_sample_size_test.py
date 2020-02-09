
from determining_sample_size import determine_sample_size

def test():
    assert  round(determine_sample_size(200, 0.05), 2) == 133.33


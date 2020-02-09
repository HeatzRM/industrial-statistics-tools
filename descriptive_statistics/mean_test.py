from mean import get_mean

def test():
    assert get_mean([1,2,3,4,5,6,7,8,9,10]) == 5.5
    assert get_mean([1,2,3,4,5]) == 3.0
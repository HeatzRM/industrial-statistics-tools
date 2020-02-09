"""
When scores are grouped we multiply first each
score x by its frequency f and divide the sum of 
products xf by total frequency N

weighted_mean = summation(x*f) / n

x = score
f = frequency
n = total frequency

"""


def get_weighted_mean(items=[{}]):
    total_freq = 0
    total = 0
    for item in items:
        total = total + (item["score"] * item["freq"])
        total_freq = total_freq + item["freq"]
    return total / total_freq

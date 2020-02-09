def get_mean(items=[]):
    """
    The mean or arithmitic average is operationally defined
    as the sum of scores divided by the number of scores.

    We use the mean when the greatest reliability is desired,
    when the distribution is normal, or not greatly skewed,
    and when there is a need for further statistical computation
    of other statistic like standard deviation and correlations
    """
    return sum(items) / len(items)


def get_weighted_mean(items=[{}]):
    """
    When scores are grouped we multiply first each
    score x by its frequency f and divide the sum of 
    products xf by total frequency N

    weighted_mean = summation(x*f) / n

    x = score
    f = frequency
    n = total frequency

    """
    total_freq = 0
    total = 0
    for item in items:
        total = total + (item["score"] * item["freq"])
        total_freq = total_freq + item["freq"]
    print(total)
    return total / total_freq

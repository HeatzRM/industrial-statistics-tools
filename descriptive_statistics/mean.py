"""

The mean or arithmitic average is operationally defined
as the sum of scores divided by the number of scores.

We use the mean when the greatest reliability is desired,
when the distribution is normal, or not greatly skewed,
and when there is a need for further statistical computation
of other statistic like standard deviation and correlations
"""


def get_mean(items=[]):
    return sum(items) / len(items)

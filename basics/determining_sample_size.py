"""
    Determining sample size using Slovin's Formula

    n = N / (1 + (N*e)**2 )

    n = sample size
    N = population size
    e = margin of error

    The margin of error to be used depends on the seriousness of committing a
    Type I error. The margin of error of 0.5 is generally used in educational
    research and 0.01 in experimental research.
"""


def determine_sample_size(population_size, margin_of_error):
    return population_size / (1 + (population_size * (margin_of_error ** 2)))

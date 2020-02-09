"""
    We use frequency count to show the number of respondents
    belonging to a certain category and the percentage to
    show the proportions of respondents belonging to that category

    The percentage is the ratio of the number of cases in a category
    to the total number of cases under study times 100%.

    Formula:
        percentage(%) = (frequency / total_number_of_cases) * 100
"""


def get_percentage(frequency=0, total_number_of_cases=1):
    return (frequency / total_number_of_cases) * 100

def is_leap_year(year: int) -> bool:
    if (year%4 is 0 and year%100 is not 0) or (year%400 is 0):
                return True
    return False
    # """
    # Given a year, this function returns a boolean indicating whether or not it is a leap year.

    # :param year: an integer indicating a year.
    # :return: A boolean indicating whether or not the year parameter is a leap year.
    # """
    # pass  # implement me

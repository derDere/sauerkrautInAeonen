import argparse
from decimal import *

EON_YEARS = 2160
YEAR_DAYS = 365
DAY_HOURS = 24
HOUR_MINUTES = 60
MONTH_WEEKS = 4
WEEK_DAYS = 7
SAUERKRAUT_GROWTH_TIME_MONTH = 2
SAUERKRAUT_WORK_TIME_MINUTES = 35
SAUERKRAUT_FERMENTATION_TIME_WEEKS = 5
SAUERKRAUT_EXPIRATION_TIME_WEEKS = 6


def a2s(aeonen):
    """
    Calculates the eons to sauerkraut
    """
    a = aeonen
    a *= EON_YEARS * YEAR_DAYS * DAY_HOURS * HOUR_MINUTES
    s = ((SAUERKRAUT_GROWTH_TIME_MONTH * MONTH_WEEKS) + SAUERKRAUT_EXPIRATION_TIME_WEEKS + SAUERKRAUT_FERMENTATION_TIME_WEEKS) * WEEK_DAYS * DAY_HOURS * HOUR_MINUTES
    s += SAUERKRAUT_WORK_TIME_MINUTES
    return Decimal(a) / Decimal(s)


def main():
    parser = argparse.ArgumentParser(description="Calculates eons to sauerkraut.")
    parser.add_argument('eon', help='number of eons')
    args = parser.parse_args()
    a = int(args.eon)
    s = a2s(a)
    print(s)


if __name__=="__main__":
    main()

#!/usr/bin/env python
# coding: utf-8

#import relevant modules
import datetime

# function to print header
def print_header():
    print("---------------------------")
    print("        THE BDAY APP")
    print("---------------------------")


# function to get user's birthdate
def get_bday_from_user():
    print("Tell us your birthday")
    year = int(input("Year [YYYY] : "))
    month = int(input("Month [MM] : "))
    day = int(input("Day [DD] : "))
    
    # uses the datetime module to convert the format of the input
    birthday = datetime.datetime(year, month, day)
    return birthday


# funtion to compute days difference
def compute_days_from_dates(bdayDate, dateNow):
    date1 = dateNow
    # setting the date2 to this year but month and day of user's bday
    date2 = datetime.datetime(dateNow.year, bdayDate.month, bdayDate.day)
    compute = date1 - date2
    # basic calculation to calculate days from seconds
    days = int(compute.total_seconds() / 60 / 60 / 24)
    return days


# function to print the final output
def print_bday_info(days):
    if days < 0:
        print("Your Birthday is in {} days!".format(-days))
    elif days > 0:
        print("Your Birthday is gone now, it was {} days ago!".format(days))
    else:
        print("Your Birthday is today! HAPPY BIRTHDAY!!")


# the main function to nest all the others, we'll only need to call this function
def main():
    print_header()
    bday = get_bday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_from_dates(bday, now)
    print_bday_info(number_of_days)


# calling the main function
main()






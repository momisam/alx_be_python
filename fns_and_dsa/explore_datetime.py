# Date and time calculator
from datetime import datetime, timedelta

def display_current_datetime():
    # get current date and time
    current_date = datetime.now()
    # format as YYYY-MM-DD HH:MM:SS
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # ask the user for number of days
    days = int(input("Enter the number of days to add to the current date: "))
    # get today's date
    current_date = datetime.now()
    # create timedelta
    days_increase = timedelta(days=days)
    # calculate future date
    future_date = current_date + days_increase
    # print in YYYY-MM-DD format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# run functions
display_current_datetime()
calculate_future_date()

#Date and time calculator
import datetime

def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%M-%D, %H:%M:%S")
    print(f"Current date and time: {current_date}")


def calculate_future_date():
    #future_date = 
    date = int(input("How many days do you want to add to the current date? "))

from datetime import datetime, timedelta 



def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date(number_of_days):
    future_date = display_current_datetime() + timedelta(days=number_of_days)
    return future_date.strftime("%Y-%m-%d")
    


print(f"Current date and time: ", display_current_datetime().strftime("%Y-%m-%d %H:%M:%S"))
number_of_days = int(input("Enter the number of days to add to the current date: "))
print("Future date: ", calculate_future_date(number_of_days))





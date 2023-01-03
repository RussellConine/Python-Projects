import datetime
from datetime import timezone, timedelta

# find current UTC time
utc_time = datetime.datetime.now(timezone.utc)

# create datetime time object for opening time
open_start = datetime.time(9,0,0)

# create datetime time object for closing time
open_end = datetime.time(17,0,0)

# time zone variance vs. utc for london, new york, and portland
london_delta = timedelta(hours=0)
portland_delta = timedelta(hours=-8)
new_york_delta = timedelta(hours=-6)

# creat tuple to iterate through with name of city and time zone variance
office_tuple = (("London", london_delta),
                ("Portland", portland_delta),
                ("New York", new_york_delta))


for office in office_tuple:
    # find hour of current time in city
    current_office_time_hour = (utc_time + office[1]).hour
    # if hour in city is between the opening and closing hours of the office, then the office is open
    if current_office_time_hour > open_start.hour and current_office_time_hour < open_end.hour:
        print("The {} office is currently open. Come on in!".format(office[0]))
    # if hour in city is outside of the opening and closing hours of the office, then the office is closed
    else:
        print("The {} office is currently closed.".format(office[0]))

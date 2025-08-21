from datetime import datetime
import pytz

def convert_timezone(time_str, from_tz, to_tz):
    fmt = "%Y-%m-%d %H:%M:%S"
    naive_time = datetime.strptime(time_str, fmt)


    source_time = pytz.timezone(from_tz).localize(naive_time)


    target_time = source_time.astimezone(pytz.timezone(to_tz))
    return target_time.strftime(fmt)



time_in_ny = "2023-10-05 14:30:00"

converted = convert_timezone(time_in_ny, "US/Eastern", "UTC")
print("Converted time:", converted)
converted = convert_timezone(time_in_ny, "US/Eastern", "Asia/Tokyo")
print("Converted time:", converted)
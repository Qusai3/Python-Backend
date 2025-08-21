import re
from datetime import datetime
from zoneinfo import ZoneInfo  

def is_valid_email(email):
    """
    Returns True if the email looks valid, otherwise False.
    (This is a simple check, good for practice.)
    """
    pattern = r'^[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'  
    return re.match(pattern, email) is not None

def show_times(timezones):
    """
    Prints the current date/time in each timezone in the list.
    """
    now_utc = datetime.now(ZoneInfo("UTC"))  
    print("Current times:\n")
    for tz in timezones:
        dt = now_utc.astimezone(ZoneInfo(tz))
        print(f"{tz:20s} {dt.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":  
    emails = [
        "qusai@gmail.com",
        "omar.se@ex.co",
        "noemail@com",
        "no-at-.com", 
        "x@y.z"             
    ]

    print("Email validation: ")
    for e in emails:
        print(f" -> {'Valid' if is_valid_email(e) else 'Invalid'}")

    print("\n")

    
    zones = ["UTC", "Asia/Amman", "Europe/London", "America/New_York", "Asia/Tokyo"]
    show_times(zones) 
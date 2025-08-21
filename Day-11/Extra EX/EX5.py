import re
from datetime import datetime

def parse_log_timestamps(log):
    pattern = r'\[(\d{2})/([A-Za-z]{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) [+-]\d{4}\]'
    matches = re.findall(pattern, log)

    month_map = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }

    results = []
    for day, mon, year, hh, mm, ss in matches:
        dt = datetime(
            int(year), month_map[mon], int(day),
            int(hh), int(mm), int(ss)
        )
        results.append(dt.strftime("%Y-%m-%d %H:%M:%S"))

    return results

log_data = '127.0.0.1 - - [21/Aug/2025:10:23:45 +0000] "GET /index.html"'
print(parse_log_timestamps(log_data))
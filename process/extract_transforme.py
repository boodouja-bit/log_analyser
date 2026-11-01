
import re

pattern = r"(\w{3})\s+(\d{1,2})\s+(\d{2}:\d{2}:\d{2}):\s+(\w+)\s+(.*)"

regex = re.compile(pattern)

def extract_from_row(row):
    result = regex.search(row)

    if result:
        month = result.group(1)
        day = int(result.group(2))
        time = result.group(3)
        service = result.group(4)
        message = result.group(5)

        return {
            "month": month,
            "day": day,
            "time": time,
            "service": service,
            "message": message
        }

    return None

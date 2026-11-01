
import re

pattern = r"(\w{3})\s+(\d{1,2})\s+(\d{2}:\d{2}:\d{2})\s+(\S+)\s+(\w+)(?:\[(\d+)\])?:\s+(.*)"

regex = re.compile(pattern)


def extract_from_row(row):

    result = regex.search(row)

    if result:
        month = result.group(1)
        day = int(result.group(2))
        time = result.group(3)
        hostname = result.group(4)
        service = result.group(5)
        pid = result.group(6)
        message = result.group(7)

        return {
            "month": month,
            "day": day,
            "time": time,
            "hostname": hostname,
            "service": service,
            "pid": pid,
            "message": message
        }

    return None


if __name__ == "__main__":

    from ingestion import raw

    rows = raw.toRows('./data')

    extracted = 0
    not_extracted = 0

    for row in rows:

        data = extract_from_row(row)

        if data is not None:
            print(data)
            extracted += 1
        else:
            not_extracted += 1

    print("\n===== RESULTAT =====")
    print("Lignes lues :", len(rows))
    print("Lignes extraites :", extracted)
    print("Lignes non extraites :", not_extracted)


import gzip
import os

def toRows(path):
    rows = []

    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            if file.endswith('.gz'):
                opener = gzip.open
                mode = 'rt'
            else:
                opener = open
                mode = 'r'

            with opener(file_path, mode=mode, encoding='utf-8',
                        errors='replace') as f:
                for row in f:
                    rows.append(row.strip())

    return rows


if __name__ == "__main__":
    rows = toRows('./data')
    print("Nombre total de lignes :", len(rows))

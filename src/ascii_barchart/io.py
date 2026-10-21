import os
import csv

def load_rows(datei):
    ordner = "data"
    ganzer_pfad = os.path.join(ordner, datei)

    with open(ganzer_pfad, mode='r', encoding='utf-8', newline='') as datei:
        reader = csv.DictReader(datei)
        alles = []
        for zeile in reader:
            print(zeile['type'], zeile['value1'], zeile['value2'])
            alles.append(zeile)
    return alles
    
def average_value1_by_type(rows):

    for x in rows:
        value1 = float(x['value1'])
        value2 = float(x['value2'])
        avg = value1 + value2
        avg = avg / 2
        print(f"{x['type']}: {avg}")
    
rows = load_rows("points.csv")
averages = average_value1_by_type(rows)
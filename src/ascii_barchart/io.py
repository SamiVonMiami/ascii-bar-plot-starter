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
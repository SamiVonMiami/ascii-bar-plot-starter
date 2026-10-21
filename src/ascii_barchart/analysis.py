def average_value1_by_type(rows):

    for x in rows:
        value1 = float(x['value1'])
        value2 = float(x['value2'])
        avg = value1 + value2
        avg = avg / 2
        print(f"{x['type']}: {avg}")
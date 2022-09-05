def Read_Footballers():
    import csv
    
    with open("Footballers.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print(" ".join(row))
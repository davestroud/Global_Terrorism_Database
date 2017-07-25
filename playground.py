import csv
with open('globalterrorism.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['country_txt'], row['region_txt'])

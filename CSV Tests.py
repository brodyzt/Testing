import csv
with open('Untitled.csv', 'rb') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(', '.join(row))
# Write user data (name, age) to a CSV file, then read it back and display it.

import csv

user_data = [
    ['Name', 'Age', 'Job'],
    ['Nikhil', 20, 'AI Engineer'],
    ['Roshan', 19, 'Data Analyst']
]

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(user_data)          # write multiple rows
    # writer.writerow(['Charlie', 42, 'Developer'])  # single row

with open('output.csv', 'r', newline = '', encoding = 'utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        print(row)
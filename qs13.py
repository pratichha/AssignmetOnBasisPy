import csv

data=[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

with open('ur file.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['name','address','age'])
    for row in data:
        csv_out.writerow(row)
        print(row)
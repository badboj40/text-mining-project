import csv
import re


def remove_br(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
    
    with open('new_'+file_name, 'w') as f:
        writer = csv.writer(f)
        for row in rows:
            row[0] = re.sub(r'<br />', '', row[0])
            writer.writerow(row)


if __name__ == '__main__':
    file_name = 'IMDB_Dataset.csv'
    remove_br(file_name)
    print('Done!')
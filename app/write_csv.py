import csv


#newline='' with a csv file
def create_csv(name, header_list):
    name += '.csv'
    with open(name, 'w', newline='') as n:
        writer = csv.writer(n)
        writer.writerow(header_list)

def write_csv(name, item_list):
    name += '.csv'
    with open(name, 'a', newline='') as n:
        writer = csv.writer(n)
        writer.writerow(item_list)


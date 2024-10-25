
import csv

def read_cvs(filename):
    """ Read and output the details of CSV file. """
    try:
        with open(filename, newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for record in csv_reader:
                print(record)
    except (IOError, OSError) as file_read_error:
        print("Unable to open the csv file. Exeption: {}".format(file_read_error))



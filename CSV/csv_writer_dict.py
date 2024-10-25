import csv

def write_csv(filename, header, data):
    """ Write the provided data to the CVS file 
    :param str filename: The name of the file to which
        the data should be written
    :param list header: The header for the columns in 
        csv file
    :param list data: The list of list mapping the 
        values to the columns
    """
    try:
        with open(filename, 'w') as csv_file:
            csv_write = csv.DictWriter(csv_file, fieldnames=header )
            csv_write.writeheader()
            csv_write.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print("Unable to write the contents to csv file. \
            Exeption: {}".format(csv_file_error))
        


if __name__ == '__main__':
    header = [
        "name", "age", "gender"
    ]
    # data = [['Richard', 32, 'M'], ['Mumzul', 21, 'F'], ['Melinda', 25, 'F']]
    data = [
        {'name': 'John', 'age': '21', 'gender': 'M'},
        {'name': 'Bill', 'age': '18', 'gender': 'M'},
        {'name': 'Julia', 'age': '23', 'gender':'FM'},
        {'name': 'Jill', 'age': '18', 'gender': 'F'}
    ]
    filename = 'simple_output.csv'
    write_csv(filename, header, data)

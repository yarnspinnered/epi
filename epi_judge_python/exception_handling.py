import csv

class ColSumParseException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.line_number = args[1]

def get_col_sum(filename, col):
    csv_file = open(filename)
    line_number = 0
    csv_reader = csv.reader(csv_file)
    running_sum = 0
    try:
        for row in csv_reader:
            if len(row) < col:
                raise IndexError("Not enough columns in tis file")
            value = int(row[col])
        try:
            running_sum += int(value)
        except ValueError:
            print("Ignoring as not value: ", value)
        line_number += 1
    except csv.Error:
        print("Error in parsing")
        raise ColSumParseException("Error in parsing at line: ", line_number)
    else:
        print("Sum = " + str(running_sum))
    finally:
        csv_file.close()
        return running_sum
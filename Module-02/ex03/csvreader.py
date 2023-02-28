import csv


class CsvReader():
    def __init__(self,
                 filename=None,
                 sep=',',
                 header=False,
                 skip_top=0,
                 skip_bottom=0):
        if (not (isinstance(filename, str) and
                 isinstance(sep, str) and
                 isinstance(header, bool) and
                 isinstance(skip_top, int) and
                 isinstance(skip_bottom, int))):
            exit("Wrong arguments")
        self.filename = filename
        self.sep = sep
        self.has_header = header
        self.skip_top = skip_top + header
        self.skip_bottom = skip_bottom
        self.fd = None
        self.data = []
        self.header = None

    def __enter__(self):
        try:
            self.fd = open(self.filename, 'r')
            csv_reader = csv.reader(self.fd, delimiter=self.sep)
        except Exception:
            return (None)

        expected_len = None
        for i, row in enumerate(csv_reader):
            if (expected_len is None):
                expected_len = len(row)
            elif (expected_len != len(row)):
                return None

            # check if there is empty line
            for element in row:
                if (len(element) == 0):
                    return None

            if (i == 0 and self.has_header is True):  # set the header
                self.header = row
            elif (i >= self.skip_top and
                    (self.skip_bottom == 0 or i < self.skip_bottom)):
                self.data.append(row)
        return (self)

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if (hasattr(self, 'fd') and self.fd is not None):
            self.fd.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        return (self.data)

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return (self.header)


if __name__ == "__main__":
    with CsvReader('../good.csv', header=True) as file:
        if (file is None):
            print("File is corrupted")
        else:
            data = file.getdata()
            # print(data)
            header = file.getheader()
            # print(header)
            print("File is good")

    with CsvReader('../bad.csv') as file:
        if (file is None):
            print("File is corrupted")
        else:
            data = file.getdata()
            # print(data)
            header = file.getheader()
            # print(header)
            print("File is good")

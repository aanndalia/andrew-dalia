"""
GP Renewables Assignment

Note: Checked with PEP8 compliance tool at http://pep8online.com/checkresult
Note 2: This was run using Python 2.7

By: Andrew Dalia
"""

import argparse


def readDataFromFileWithDelimiter(fileName, delimiter):
    """
    Reads the data from a file and splits each line by the provided delimiter

    :param fileName: The file to read
    :type fileName: str
    :param delimiter: The delimiter to split each line by
    :type delimiter: str

    :rtype: list
    """
    if not fileName:
        print "There is no file data to read"
        return []

    with open(fileName) as f:
        dataLines = [line.strip().split(delimiter) for line in f]

    return dataLines


def normalizeData(data, columnOrder):
    """
    Reorders the data for each row in the given data based on the columnOrder
    passed in

    :param data: the data being processed
    :type data: list
    :param columnOrder: the order in which the row should be reorganized
    :type columnOrder: tuple

    :rtype: list
    """
    if not data or len(columnOrder) != len(data[0]):
        return []

    normalizedData = [[row[cell] for cell in columnOrder] for row in data]
    return normalizedData


def readAllData():
    """
    Reads the data from the differently formatted files into a common container

    The fileToOrderDict dictionary has the order in which the columns appear
    in the output as a tuple value. For example, for the pipe file column 0 in
    the output is at column 1 in pipe and column 1 in the output as at column
    0 in pipe.

    The fileToDelimterDict has a mapping from the file to the delimiter so we
    know how to split each line.

    The data is read from file line by line and split by the delimiter and
    then normalized by the column order

    The final output is sorted by the first column which (last name) which is
    the default ordering the output should have.
    """
    fileToOrderDict = {'pipe': (1, 0, 2, 3), 'csv': (1, 2, 0, 3),
                       'slash': (2, 1, 3, 0)}
    fileToDelimiterDict = {'pipe': ' | ', 'csv': ', ', 'slash': '/'}
    allData = []
    for fileName, delimiter in fileToDelimiterDict.iteritems():
        allData.extend(normalizeData(readDataFromFileWithDelimiter(
            fileName, delimiter), fileToOrderDict[fileName]))
    return allData


def sortData(data, reverseOrder=False, sortColumn=0):
    """
    Reverses the data set by last name column

    :param data: the data being processed
    :type data: list
    :param reverseOrder: whether to sort the data in reverse order
    :type reverseOrder: bool
    :param sortColumn: the column to sort by
    :type sortColumn: int

    :rtype: list
    """
    if not data:
        return []

    return sorted(data, key=lambda row: row[sortColumn], reverse=reverseOrder)


def filterByAllFields(data, filterString):
    """
    Filter the data set by looking if the filterString is present in
    any of the columns

    :param data: the data being processed
    :type data: list
    :param filterString: the string to filter by
    :type filterString: str

    :rtype: list
    """
    if not data:
        return []

    filteredData = filter(lambda row: any(
        filterString in cell for cell in row), data)
    return filteredData


def processData(data, dataFilter, reverseMode, yearSortMode):
    """
    Processes the data by applying the correct action for each of the optional
    command line arguments

    :param data: the data being processed
    :type data: list
    :param dataFilter: the string to filter the rows by
    :type dataFilter: str
    :param reverseMode: indicates whether to reverse the order of the rows
                        based on last name or year published
    :type reverseMode: bool
    :param yearSortMode: indicates the data set should be sorted by year
    :type yearSortMode: bool

    :rtype: list
    """
    if not data:
        return []

    processedData = data
    if dataFilter:
        processedData = filterByAllFields(processedData, dataFilter)

    sortColumn = 3 if yearSortMode else 0
    processedData = sortData(processedData, reverseOrder=reverseMode,
                             sortColumn=sortColumn)

    return processedData


def printData(data):
    """
    Prints the data rows line by line

    :param data: the data being processed
    :type data: list
    """
    if not data:
        print "No data to display"
        return

    for line in data:
        print ', '.join(line)
    print "\n"


def getArgs():
    """
    Parses and gets all the arguments passed in by command line using argparse.
    Comes with information to display a help menu.

    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description='Show a list of books, '
                        'alphabetical ascending by author\'s name by default')
    parser.add_argument('-f', '--filter', help='show a subset of books, looks'
                        'for the argument as a substring of any of the fields')
    parser.add_argument('--year', help='sort the books by year, ascending'
                        'instead of default sort', action='store_true')
    parser.add_argument('--reverse', help='reverse sort', action='store_true')
    args = parser.parse_args()
    return args


def main():
    inputArgs = getArgs()
    data = readAllData()
    dataFilter = inputArgs.filter
    reverseMode = inputArgs.reverse
    yearSortMode = inputArgs.year
    dataOutput = processData(data, dataFilter, reverseMode, yearSortMode)
    printData(dataOutput)


main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This program retrieves a CSV from a URL, processes it, searches for file
 extensions, and calculates percentages for specific categories.
"""

import csv


def downloadData(url):
    """
    Args:
        url (str): URL for fetching of data.
    Returns:
        data (str): Contents of string from URL response data.
    Example:
        >> downloadData(url)
        >>
    """
    # Generates HTTP request for the passed 'url'; returns/stores HTTP response.
    response = urllib2.urlopen(url)
    # Sets 'data' to the contents of 'response'.
    data = response.read()
    return data


def processData(response_data):
    """
    Args:
        response_data (str): Contents of data from downloadData function.
    Returns:
        myresult_dict (dict): Dictionary file containing formatted records.
    Example:
        >> processData(csvdata)
        >>
    """
    # Creates dict 'myresult_dict'.
    myresult_dict = {}
    # Splits the string on each '\n' delimiter and stores each in 'response_list'.
    response_list = response_data.split("\n")
    # For each line in 'response_list' within specified range...
    for rec_line in response_list[1:-1]:
        # Split each line on ',' delimiter
        rec = rec_line.split(",")
        try:
            # Add formatted and indexed values from 'rec' into the dictionary.
            #myresult_dict[rec[0]] = (rec[1], datetime.datetime.strptime(rec[2], "%d/%m/%Y"))
            myresult_dict[rec[0]] = (rec[1], (rec[2], "%d/%m/%Y"))
        except (ValueError):
            # Write formatted error message to log file.
            print 'Error processing line {} for *** {}'.format(rec_line[0], rec[0])
            pass
        else:
            pass

    return myresult_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Enter the data url')
    args = parser.parse_args()
    if args.url:
        url = ''
        csvdata = downloadData(url)
        result = processData(csvdata)
        records = displayPerson(id, result)
    else:
        print 'error'

if __name__ == '__main__':
    main()
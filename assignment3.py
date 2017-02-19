#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This program retrieves a CSV from a URL, processes it, searches for file
 extensions, and calculates percentages for specific categories.
"""

import csv, urllib2, re


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
    # Creates dict, 'browsers', with default values.
    browsers = {'Firefox':0,
                'Chrome':0,
                'Internet Explorer':0,
                'Safari':0}
    # Creates dict, 'imghits', with default values.
    imghits = {'img':0,
               'rowcount':0}

    # Creates csv reader object, 'reader'.
    #reader = csv.reader(response_data.split("\n"))
    # For each line in 'response_list' within specified range...
    for row in csv.reader(response_data):
    #for row in reader:
        # Count total number of page hits while in loop.
        imghits['rowcount'] += 1
        if re.search(r"(?i)(jpg|jpeg)|gif|png", row[0]):
            imghits['img'] += 1
        if re.search("firefox", row[2]):
           browsers['Firefox'] += 1
        elif re.search(r"Chrome", row[2]):
           browsers['Chrome'] += 1
        elif re.search(r"MSIE", row[2]):
           browsers['Internet Explorer'] += 1
        elif re.search(r'Safari', row[2]):
            browsers['Safari'] += 1

    # Determine the percentage imghits and print result.
    imgcalc = (float(imghits['img'])) / (float(imghits['rowcount'])) * 100
    print "Image requests account for {}% of all requests.".format(imgcalc)
    # Determine most popular browser and print result.
    maximum = max(browsers, key=browsers.get)
    print "The most popular browser is {}.".format(maximum)

def main():
    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
    csvdata = downloadData(url)
    processData(csvdata)
"""
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Enter the data url')
    args = parser.parse_args()
    if args.url:
        # http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv
        url = ''
        csvdata = downloadData(url)
        result = processData(csvdata)
    else:
        print 'error'
"""

if __name__ == '__main__':
    main()
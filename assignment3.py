#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This program retrieves a CSV from a URL, processes it, searches for file
 extensions, and calculates percentages for specific categories.
"""


import argparse, urllib2, csv, re


def download_data(url):
    """
    Args:
        url (str): URL for fetching of data.
    Returns:
        data (str): Contents of string from URL response data.
    Example:
        >> downloadData(url)
        >>
    """
    data_content = urllib2.urlopen(url)
    return data_content


def process_data(response_data):
    """
    Args:
        response_data (str): Contents of data from downloadData function.
    Returns:
        imgcalc (float): Floating point value for percentage of image hits.
        maximum (int): Highest integer value for browsers.
    Example:
        >> process_data(csvdata)
        >>
    """
    browsers = {'Firefox': 0,
                'Chrome': 0,
                'Internet Explorer': 0,
                'Safari': 0}

    imghits = {'img': 0,
               'rowcount': 0}

    for row in csv.reader(response_data):
        imghits['rowcount'] += 1
        if re.search(r"(?i)(jpg|jpeg)|gif|png", row[0]):
            imghits['img'] += 1
        if re.search("MSIE", row[2]):
            browsers['Internet Explorer'] += 1
        elif re.search("Chrome", row[2]):
            browsers['Chrome'] += 1
        elif re.search("firefox", row[2], re.I):
            browsers['Firefox'] += 1
        elif re.search("Safari", row[2]) and not re.search("Chrome", row[2]):
            browsers['Safari'] += 1

    imgcalc = (float(imghits['img'])) / (float(imghits['rowcount'])) * 100
    print "Image requests account for {}% of all requests.".format(imgcalc)

    maximum = max(browsers, key=browsers.get)
    print "The most popular browser is {}.".format(maximum)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Enter the data url')
    args = parser.parse_args()

    if args.url:
        #url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
        csvdata = download_data(args.url)
        process_data(csvdata)
    else:
        print 'error'

if __name__ == '__main__':
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This program retrieves a CSV from a URL, processes it, searches for file
 extensions, and calculates percentages for specific categories.
"""

import argparse, urllib2, csv, re


def download_data(url):
    data_content = urllib2.urlopen(url)
    return data_content


def process_data(content):
    counts = {'imagehit':0,
              'rowcount':0}

    browsers = {'Internet Explorer':0,
                'Firefox':0,
                'Google Chrome':0,
                'Safari':0}

    for line in csv.reader(content):
        counts['rowcount'] += 1
        if re.search(r"(?i)(jpg|jpeg)|gif|png", line[0]):
            counts['imagehit'] += 1
        if re.search("MSIE", line[2]):
            browsers['Internet Explorer'] += 1
        elif re.search("Chrome", line[2]):
            browsers['Google Chrome'] += 1
        elif re.search("firefox", line[2], re.I):
            browsers['Firefox'] += 1
        elif re.search("Safari", line[2]) and not re.search("Chrome", line[2]):
            browsers['Safari'] += 1

    image_cal = (float(counts['imagehit'])/ counts['rowcount']) * 100
    top_browsed = [max(b for b in browsers.items())]
    resultname = top_browsed[0][0]
    resultnum = top_browsed[0][1]

    report = ("There's a total of {} page hits today.\n"
              "Images account for {} % percent of all requests.\n"
              "{} is browser top used with {} hits.").format(counts['rowcount'],
                                                             image_cal,
                                                             resultname,
                                                             resultnum)
    print report


def main():
    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
    inf = download_data(url)
    process_data(inf)

if __name__ == '__main__':
    main()
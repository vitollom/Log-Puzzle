#!/usr/bin/env python2
"""
Log Puzzle exercise

Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

Given an Apache logfile, find the puzzle URLs and download the images.

Here's what a puzzle URL looks like (spread out onto multiple lines):
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg
HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US;
rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

import os
import re
import sys
import urllib.request
import argparse


def read_urls(filename):
    """Returns a list of the puzzle URLs from the given log file,
    extracting the hostname from the filename itself, sorting
    alphabetically in increasing order, and screening out duplicates.
    """
    img_urls = []
    prefix = filename.split("_")[-1]
    pattern = re.compile(r"\/\S*\/puzzle\/\S*")

    with open(filename, "r") as f:
        contents = f.read()
        all_urls = pattern.finditer(contents)
        for match in all_urls:
            url = "https://" + prefix + match.group(0)
            if url not in img_urls:
                img_urls.append(url)
        f.close()

    img_urls.sort(key=lambda img: img.split("-")[-1])
    return img_urls


def download_images(img_urls, dest_dir):
    """Given the URLs already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory with an <img> tag
    to show each local image file.
    Creates the directory if necessary.
    """
    if dest_dir not in os.listdir():
        os.makedirs(dest_dir)

    os.chdir(dest_dir)

    for url in img_urls:
        index = img_urls.index(url)
        urllib.request.urlretrieve(url, filename=f"img{index}.jpg")
        print(f"Retrieving {url}...")
    print("Complete")

    img_tag_list = []
    html_tag_list = ["<html>\n", "<body>\n"]

    for file in os.listdir():
        if file.endswith(".jpg"):
            img_tag_list.append(f"<img src={str(file)}>")

    def sort_helper(tag):
        tag_split = tag.split(".")[0]
        return int(tag_split.split("g")[2])

    img_tag_list.sort(key=sort_helper)
    img_tag_list.extend(["</body>\n", "</html>\n"])
    html_tag_list.extend(img_tag_list)

    with open("index.html", "w") as f:
        f.writelines(img_tag_list)
        f.close()
    pass


def create_parser():
    """Creates an argument parser object."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--todir',
                        help='destination directory for downloaded images')
    parser.add_argument('logfile', help='apache logfile to extract urls from')

    return parser


def main(args):
    """Parses args, scans for URLs, gets images from URLs."""
    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)

    img_urls = read_urls(parsed_args.logfile)

    if parsed_args.todir:
        download_images(img_urls, parsed_args.todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main(sys.argv[1:])

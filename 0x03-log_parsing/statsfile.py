#!/usr/bin/env python3
"""reads standard input and generates required reports from it"""

# read for the text file line by line
# keep the number of lines read
# extract the file size during reading each line -> adding to total filesize
# after reading 10 line print the required statistics
import os
import re

file_path = 'testinput.txt'

if not os.path.exists(file_path):
    print(f"File {file_path} not found!")

# 192.168.32.11 - [2024-01-15 23:31:09.549076]28 "GET /projects/260 HTTP/1.1" 200 10


def extract(line):
    match = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s", line)
    if match:
        return match.group(1)
    return None


with open(file_path, 'r') as file:
    for line in file:
        date = extract(line)
    print(date)

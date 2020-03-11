import time
import serial
import csv
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data_file = os.path.join(__location__, "02-move")

with open(data_file, newline="\n") as csvfile:
    frames = csv.reader(csvfile, delimiter=',') #, quotechar='|')
    skip_header = True
    for row in frames:
        if skip_header:
            skip_header = False
        else:
            print(', '.join(row))

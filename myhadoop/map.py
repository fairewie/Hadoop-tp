#!/usr/bin/env python
import sys
from datetime import datetime

def prepare_for_aggregation(line):
    fields = line.strip().split(',')
    timestamp = datetime.strptime(fields[0], "%Y-%m-%d %H:%M:%S")
    amplitude = float(fields[5])  
    print(f"agg\t{timestamp.date()}\t{amplitude}")

def mark_for_correlation_analysis(line):
    fields = line.strip().split(',')
    timestamp = datetime.strptime(fields[0], "%Y-%m-%d %H:%M:%S")
    location = fields[1] + fields[2]  
    magnitude = float(fields[5])

    print(f"corr\t{timestamp}\t{location}\t{magnitude}")

for line in sys.stdin:
    prepare_for_aggregation(line)
    mark_for_correlation_analysis(line)

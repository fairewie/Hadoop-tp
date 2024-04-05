#!/usr/bin/env python
import sys

def aggregate_amplitude(data):
    amplitudes = [float(item.split('\t')[2]) for item in data]
    average_amplitude = sum(amplitudes) / len(amplitudes)
    print(f"Aggregated Data: Average Amplitude = {average_amplitude}")

def analyze_correlation(data):
    locations = {}
    for item in data:
        _, timestamp, location, magnitude = item.split('\t')
        if location not in locations:
            locations[location] = 1
        else:
            locations[location] += 1
    
    for location, count in locations.items():
        print(f"Location: {location}, Event Count: {count}")

current_key = None
current_data = []

for line in sys.stdin:
    line = line.strip()
    key, rest = line.split('\t', 1)
    
    if key != current_key:
        if current_key == "agg":
            aggregate_amplitude(current_data)
        elif current_key == "corr":
            analyze_correlation(current_data)
        current_data = []
        current_key = key
    
    current_data.append(line)

if current_key == "agg":
    aggregate_amplitude(current_data)
elif current_key == "corr":
    analyze_correlation(current_data)

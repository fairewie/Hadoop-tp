#!/usr/bin/env python

import sys

def clean_data(line):
    fields = line.strip().split(',')
    # Supposons que les champs importants sont les suivants :
    # 0: Date, 1: Heure, 2: Latitude, 3: Longitude, 4: Profondeur, 5: Magnitude
    if len(fields) < 6:
        return None  # Ligne incomplète
    try:
        magnitude = float(fields[5])
        if magnitude < 0 or magnitude > 10:
            return None  # Magnitude aberrante
    except ValueError:
        return None  # Erreur de conversion (valeur non numérique pour la magnitude)
    # La ligne passe tous les filtres
    return line

for line in sys.stdin:
    cleaned_line = clean_data(line)
    if cleaned_line:
        print(cleaned_line)
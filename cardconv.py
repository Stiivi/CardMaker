# cardconv.py
#
# Convert .csv file into JSON cards file
#
# Result JSON is a dictionary and has the following items:
# 
# cards - array of cards
#

import json
import csv
import sys

if len(sys.argv) < 3:
    print("Usage: cardconv.py INPUT_CSV OUTPUT_JSON")
    exit(1)

card_file = sys.argv[1]
json_file = sys.argv[2]

result = {
    "cards": []
}

with open(card_file) as file:
    reader = csv.DictReader(file)
    for record in reader:
        result["cards"].append(record)

with open(json_file, "w") as file:
    json.dump(result, file)

import pandas as pd
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Split Excel file into text files')

# Add an argument
parser.add_argument('file', type=str, help='The Excel file to split')

# Parse the arguments
args = parser.parse_args()

# Read the excel file
df = pd.read_excel(args.file)

# Iterate over the rows
for index, row in df.iterrows():
    # Open a file with name from column 'A' and write column 'B' into it
    with open(str(row['A']) + '.txt', 'w') as f:
        f.write(str(row['B']))

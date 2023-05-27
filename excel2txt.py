import pandas as pd

# read the excel file
df = pd.read_excel('ekkeli.xlsx')

# iterate over the rows
for index, row in df.iterrows():
    # open a file with name from column 'A' and write column 'B' into it
    with open(str(row['File']) + '.txt', 'w') as f:
        f.write(str(row['Content']))

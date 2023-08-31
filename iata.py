import pandas as pd

# Read the data from the .txt file
data = []
with open('text.txt', 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        data.append(parts)

# Convert the data into a DataFrame
columns = ['Code', 'City', 'Country']
df = pd.DataFrame(data, columns=columns)

#print(df)

# Create an Excel file
excel_file = 'iata_codes.xlsx'
df.to_excel(excel_file, index=False)

print(f"Excel file '{excel_file}' created successfully.")

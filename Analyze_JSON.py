import pandas as pd

# Load the uploaded Excel file
file_path = '/Users/karsten/Downloads/Thesis/Results/Definief!.xlsx'
xls = pd.ExcelFile(file_path)

# Load the sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name='Proposals')

# Function to extract networks, strategies, and symbols from a JSON string
def extract_from_json(json_str):
    data = eval(json_str)
    networks = []
    strategies = []
    symbols = []
    
    for entry in data:
        network = entry.get('network', '')
        symbol = entry['params'].get('symbol', '')
        if 'strategies' in entry['params']:
            for strategy in entry['params']['strategies']:
                networks.append(str(strategy.get('network', '')))
                strategies.append(str(strategy.get('name', '')))
                symbols.append(symbol)
        else:
            networks.append(str(network))
            symbols.append(symbol)
    
    return ','.join(networks), ','.join(strategies), ','.join(symbols)

# Extracting data from the 'strategies' column
df[['networks', 'strategies', 'symbols']] = df['strategies'].apply(lambda x: pd.Series(extract_from_json(x)))

# Display the new DataFrame with the extracted columns
print(df[['networks', 'strategies', 'symbols']])

# Save the original DataFrame and the extracted columns to a new sheet in the same Excel file
output_file_path = '/Users/karsten/Downloads/Thesis/Results/Copy_Final_Version3.xlsx'
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Proposals', index=False)
    df[['networks', 'strategies', 'symbols']].to_excel(writer, sheet_name='Extracted Data', index=False)

output_file_path

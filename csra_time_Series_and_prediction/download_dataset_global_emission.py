import pandas as pd
import requests

# https://ourworldindata.org/co2-dataset-sources
# Fetch the data.
data_url = "https://ourworldindata.org/grapher/annual-co2-emissions-per-country.csv?v=1&csvType=full&useColumnShortNames=false"
df = pd.read_csv(
    data_url,
    storage_options={'User-Agent': 'Our World In Data data fetch/1.0'})

# Fetch the metadata (optional, but good practice to keep it)
metadata_url = "https://ourworldindata.org/grapher/annual-co2-emissions-per-country.metadata.json?v=1&csvType=full&useColumnShortNames=false"
metadata = requests.get(metadata_url).json()

# Print the first few rows of the DataFrame (optional)
print(df.head())

# Print the metadata (optional)
print(metadata)

# Save the DataFrame to a CSV file
output_filename = "dataset/global_co2_emissions.csv"
df.to_csv(output_filename, index=False)  # index=False prevents writing row numbers to the file

print(f"Data saved to {output_filename}")

# Save the metadata to a json file
import json

output_metadata_filename = "global_co2_emissions_metadata.json"
with open(output_metadata_filename, 'w') as f:
    json.dump(metadata, f, indent=4)

print(f"Metadata saved to {output_metadata_filename}")

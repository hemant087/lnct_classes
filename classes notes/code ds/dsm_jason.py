import pandas as pd

# Read the file
with open("cleaned_data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Process each line
structured_data = []
for line in lines:
    parts = line.strip().split(":")  # Assuming 'Key: Value' format
    if len(parts) == 2:
        key, value = parts
        structured_data.append({key.strip(): value.strip()})

# Convert to DataFrame
df = pd.DataFrame(structured_data)

# Save to CSV
df.to_csv("structured_data.csv", index=False)

print(df)

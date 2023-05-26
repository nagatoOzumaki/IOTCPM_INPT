import pandas as pd

# Read the CSV file
df = pd.read_csv(
    "dataset_sensors.csv")

df['time'] = pd.to_datetime(df['time']).astype(int) // 10**6
df['time'] = df['time'].astype(str)

lines = []
for _, row in df.iterrows():
    tags = ','.join([f'{key}={value}' for key, value in row[1:].items()])
    line = f"energy {tags} {row['time']}"
    lines.append(line.strip())

with open('convertedToLineProtocol.txt', 'w') as file:
    file.write('\n'.join(lines))

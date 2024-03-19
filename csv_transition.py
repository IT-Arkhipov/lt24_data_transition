import sys
import json
import pandas as pd
from warnings import simplefilter

from lib.utls import insert_df_value

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
json_filename = 'orders_3.json'
csv_filename = 'converted_json.csv'

if sys.stdin.isatty():
    if len(sys.argv) != 2:
        print("Usage: python csv_transition.py <filename>")
        sys.exit(1)

    json_filename = sys.argv[1]

try:
    with open(json_filename, 'r', encoding='utf-8') as file:
        orders = json.load(file)
except FileNotFoundError:
    print(f"File '{json_filename}' not found.")


df = pd.DataFrame()

for order in orders:
    new_row = pd.DataFrame({}, index=[0])
    df = pd.concat([df, new_row], ignore_index=True)
    insert_df_value(order, df)

int_columns = ['date', 'departure_parks', 'arrival_parks', 'start_time', 'end_time', 'plan_time', 'load_time',
               'created', 'version', 'modified', 'duration', 'photos', 'files', 'tags']
for column in df.columns:
    if 'tags' in column:
        df[column] = df[column].fillna(0)
    if any(string in column for string in int_columns):
        df[column] = df[column].astype('int64')
df = df.infer_objects(copy=False).fillna('')
df.to_csv(csv_filename)

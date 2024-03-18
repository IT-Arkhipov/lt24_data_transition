import sys
import json
import pandas as pd
from warnings import simplefilter

custom_fields_limit = 3
list_limit = 3

skipped_key = ['goods', 'states_history']


def insert_df_value(data, _df, prefix=''):
    for key, value in data.items():
        if key in skipped_key:
            continue
        new_key = f"{prefix}{key}" if prefix else key
        if isinstance(value, dict):
            insert_df_value(value, _df, prefix=new_key + '_')
        elif 'custom_fields' in new_key:
            for custom_field in value[:custom_fields_limit]:
                _df.loc[_df.index[-1], f"{new_key}_{custom_field.get('id')}"] = custom_field.get('value')
        elif 'banned_tags' in new_key:
            for tag in value[:list_limit]:
                _df.loc[_df.index[-1], f"{new_key}_{tag}"] = 1
        elif 'required_vehicle_tags' in new_key:
            for tag in value[:list_limit]:
                _df.loc[_df.index[-1], f"{new_key}_{tag}"] = 1
        elif 'tags' in new_key:
            for tag in value[:list_limit]:
                _df.loc[_df.index[-1], f"{new_key}_{tag}"] = 1
        elif 'photos' in new_key or 'files' in new_key:
            _df.loc[_df.index[-1], new_key] = len(value)
        elif 'parks' in new_key and 'lated_by_parks' not in new_key:
            if value:
                _df.loc[_df.index[-1], new_key] = value[-1].get('end') - value[-1].get('begin')
            else:
                _df.loc[_df.index[-1], new_key] = 0
        elif 'zones' in new_key:
            if value:
                _df.loc[_df.index[-1], new_key] = value[0]
            else:
                _df.loc[_df.index[-1], new_key] = ''
        else:
            if isinstance(value, str):
                value = value.replace('\n', '').replace(',', '')
            _df.loc[_df.index[-1], new_key] = value
    return _df


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

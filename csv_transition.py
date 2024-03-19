import pandas as pd
from warnings import simplefilter

from lib import dataset
from lib.api import get
from lib.utls import insert_df_value

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
csv_filename = 'converted_json.csv'

orders = get.orders(*dataset.ALL_DATES)

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

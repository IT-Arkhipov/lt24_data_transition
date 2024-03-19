import argparse
import pandas as pd

from datetime import datetime
from warnings import simplefilter
from lib import init, dataset
from lib.api import get
from lib.definition import settings, credentials
from lib.utls import insert_df_value

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

settings.base_url = init.config['test_env']['url']
credentials.login = init.config['credentials']['login']
credentials.password = init.config['credentials']['password']
settings.session_id = init.get_session_id()

parser = argparse.ArgumentParser(description="Process a file and a date.")
parser.add_argument("filename", type=str, help="The file to process")
parser.add_argument('-d', '--date', type=lambda d: int(datetime.strptime(d, '%d.%m.%Y').timestamp() + 10_800) * 1_000,
                    help='The date in DD.MM.YYYY format')
args = parser.parse_args()

filename = args.filename
get_orders_date = args.date
if not filename:
    filename = 'converted_json.csv'
if not get_orders_date:
    get_orders_date = dataset.GET_ORDERS_DATES

orders = get.orders(get_orders_date, get_orders_date)
print(f"{len(orders)} to proceed")

df = pd.DataFrame()

order_count = 0
for order in orders:
    new_row = pd.DataFrame({}, index=[0])
    df = pd.concat([df, new_row], ignore_index=True)
    insert_df_value(order, df)
    if order_count % 100 == 0 and order_count // 100 > 0:
        print(f"{order_count // 100 * 100} orders passed")
    order_count += 1

print(f">>> {order_count} orders converted! <<<")

int_columns = ['date', 'departure_parks', 'arrival_parks', 'start_time', 'end_time', 'plan_time', 'load_time',
               'created', 'version', 'modified', 'duration', 'photos', 'files', 'tags']
for column in df.columns:
    if 'tags' in column:
        df[column] = df[column].fillna(0)
    if any(string in column for string in int_columns):
        df[column] = df[column].astype('int64')
df = df.infer_objects(copy=False).fillna('')

df.to_csv(filename)

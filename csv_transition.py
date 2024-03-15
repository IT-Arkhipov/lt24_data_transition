import json
import pandas as pd
from warnings import simplefilter

custom_fields_limit = 3
list_limit = 3

skipped_key = ['goods', 'states_history']


def init_df(data, _df, prefix=''):
    for key, value in data.items():
        if key in skipped_key:
            continue
        new_key = f"{prefix}{key}" if prefix else key
        if isinstance(value, dict):
            init_df(value, _df, prefix=new_key + '_')
        elif 'custom_fields' in new_key:
            for custom_field in value[:custom_fields_limit]:
                _df[f"{new_key}_{custom_field.get('id')}"] = [custom_field.get('value')]
        elif 'banned_tags' in new_key:
            for tag in value[:list_limit]:
                _df[f"{new_key}_{tag}"] = 1
        elif 'required_vehicle_tags' in new_key:
            for tag in value[:list_limit]:
                _df[f"{new_key}_{tag}"] = 1
        elif 'tags' in new_key:
            for tag in value[:list_limit]:
                _df[f"{new_key}_{tag}"] = 1
        elif 'photos' in new_key or 'files' in new_key:
            _df[new_key] = len(value)
        elif 'parks' in new_key and 'lated_by_parks' not in new_key:
            if value:
                _df[new_key] = value[-1].get('end') - value[-1].get('begin')
            else:
                _df[new_key] = 0
        elif 'zones' in new_key:
            if value:
                _df[new_key] = value[0]
            else:
                _df[new_key] = ''
        # elif isinstance(value, list):
        #     for i, element in enumerate(value[:list_limit]):
        #         if isinstance(element, (dict, list, set, tuple)):
        #             init_df(element, _df, prefix=f"{new_key}_{i}_")
        #         else:
        #             _df[f"{new_key}"] = element
        #     else:
        #         _df[f"{new_key}"] = ''
        else:
            _df[new_key] = [value]
    return _df


def add_to_df(_index, data, _df, prefix=''):
    for key, value in data.items():
        if key in skipped_key:
            continue
        new_key = f"{prefix}{key}" if prefix else key
        if isinstance(value, dict):
            add_to_df(_index, value, _df, prefix=new_key + '_')
        elif 'custom_fields' in new_key:
            for custom_field in value[:custom_fields_limit]:
                _df.loc[_index, f"{new_key}_{custom_field.get('id')}"] = custom_field.get('value')
        elif 'banned_tags' in new_key:
            for tag in value[:list_limit]:
                _df.loc[_index, f"{new_key}_{tag}"] = 1
        elif 'required_vehicle_tags' in new_key:
            for tag in value[:list_limit]:
                _df.loc[_index, f"{new_key}_{tag}"] = 1
        elif 'tags' in new_key:
            for tag in value[:list_limit]:
                _df.loc[_index, f"{new_key}_{tag}"] = 1
        elif 'photos' in new_key or 'files' in new_key:
            _df.loc[_index, new_key] = len(value)
        elif 'parks' in new_key and 'lated_by_parks' not in new_key:
            if value:
                _df.loc[_index, new_key] = value[-1].get('end') - value[-1].get('begin')
            else:
                _df.loc[_index, new_key] = 0
        elif 'zones' in new_key:
            if value:
                _df.loc[_index, new_key] = value[0]
            else:
                _df.loc[_index, new_key] = ''
        # elif isinstance(value, list):
        #     for i, element in enumerate(value[:list_limit]):
        #         if isinstance(element, (dict, list, set, tuple)):
        #             add_to_df(_index, element, _df, prefix=f"{new_key}_{i}_")
        #         else:
        #             _df.loc[_index, f"{new_key}"] = element
        #     else:
        #         _df.loc[_index, f"{new_key}"] = ''
        else:
            _df.loc[_index, new_key] = value
    return _df


with open('orders_3.json', 'r', encoding='utf-8') as file:
    # Load JSON data from the file
    orders = json.load(file)

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

df = pd.DataFrame()

init_df(orders[0], df)
if len(orders) > 1:
    for index, order in enumerate(orders[1:]):
        add_to_df(index + 1, order, df)

# for column in df.columns:
#     if 'custom_fields' in column:
#         df[column] = df[column].fillna(0)
# df = df.fillna('')
df.to_csv('sample_dataframe.csv', sep=';')

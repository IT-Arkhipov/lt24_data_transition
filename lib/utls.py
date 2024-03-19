from lib import dataset


def insert_df_value(data, _df, prefix=''):
    for key, value in data.items():
        if key in dataset.skipped_key:
            continue
        new_key = f"{prefix}{key}" if prefix else key
        if isinstance(value, dict):
            insert_df_value(value, _df, prefix=new_key + '_')
        elif 'custom_fields' in new_key:
            for custom_field in value[:dataset.custom_fields_limit]:
                _df.loc[_df.index[-1], f"{new_key}_{custom_field.get('id')}"] = custom_field.get('value')
        elif 'banned_tags' in new_key:
            for tag in value[:dataset.list_limit]:
                _df.loc[_df.index[-1], f"{new_key}_{tag}"] = 1
        elif 'required_vehicle_tags' in new_key:
            for tag in value[:dataset.list_limit]:
                _df.loc[_df.index[-1], f"{new_key}_{tag}"] = 1
        elif 'tags' in new_key:
            for tag in value[:dataset.list_limit]:
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

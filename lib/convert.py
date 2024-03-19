import time

from datetime import timedelta, datetime, timezone


def str_to_time(time_str) -> int:
    if not time_str:
        return 0
    x = time.strptime(time_str, "%H:%M:%S")
    return int(timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()) * 1000


def str_to_date_time(time_str) -> int:
    try:
        local_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        utc_timestamp = local_time.replace(tzinfo=timezone.utc).timestamp()
        return int(utc_timestamp) * 1000
    except ValueError:
        return 0


def current_date_timestamp() -> int:
    current_utc_time = datetime.now(timezone.utc)
    current_utc_date = current_utc_time.replace(hour=0, minute=0, second=0, microsecond=0)
    return int(current_utc_date) * 1000


def time_to_str(timestamp: [int, float]) -> str:
    return str(datetime.utcfromtimestamp(timestamp // 1000)) if timestamp else ''


def ymd_to_dmy(date_time: str) -> str:
    if not date_time:
        return ''
    return datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %H:%M:%S')


def date_from_datetime(date_time):
    return (date_time // 86400000) * 86400000

def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return ''


def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return days, hours, minutes, seconds


def dhms_to_seconds(days, hours, minutes, seconds):
    return (((days * 24) + hours) * 60 + minutes) * 60 + seconds


def dhms_to_minutes(days, hours, minutes, seconds):
    return ((days * 24) + hours) * 60 + minutes

import datetime, pytz

def currentime():
    now = datetime.datetime.now(pytz.timezone('Asia/Taipei'))
    if now.time() <= datetime.time(12, 0):
        date_time = now.replace(hour=12, minute=0, second=0, microsecond=0)
    elif now.time() <= datetime.time(16, 0):
        date_time = now.replace(hour=16, minute=0, second=0, microsecond=0)
    elif now.time() <= datetime.time(22, 0):
        date_time = now.replace(hour=22, minute=0, second=0, microsecond=0)
    else:date_time = (now + datetime.timedelta(days=1)).replace(hour=10, minute=0, second=0, microsecond=0)

    return date_time.strftime("%Y-%m-%d %H:%M:%S")
import datetime as dt

current_time = dt.datetime.now()
utc_time = dt.datetime.utcnow()
current_date = dt.date.today()
specific_date = dt.datetime(1974, 3, 9)

print(current_date)
print(utc_time)
print(current_date)
print(specific_date)

print(current_date.strftime('%Y-%y-%W-%w'))

import calendar

sep = calendar.TextCalendar(calendar.MONDAY)
sep.prmonth(1974, 3)

print(calendar.leapdays(2000, 2023))

print(calendar.prcal(2023))

for i in sep.itermonthdays(2023, 7):
    print(i)

for month in calendar.month_name:
    print(month)

for day in calendar.day_name:
    print(day)

for day_abr in calendar.day_abbr:
    print(day_abr)

for mon_abr in calendar.month_abbr:
    print(mon_abr)

hc = calendar.HTMLCalendar(calendar.MONDAY)
print(hc.formatmonth(2023, 7))

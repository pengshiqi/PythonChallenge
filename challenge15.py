import datetime
import calendar

for i in xrange(1006, 1997, 10):
    d = datetime.date(i, 1, 26)
    if d.weekday() == 0 and i % 4 == 0:
        print d
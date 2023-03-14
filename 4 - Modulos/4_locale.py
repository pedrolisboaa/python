import calendar
from datetime import datetime

import locale
locale.setlocale(locale.LC_ALL, '')

print(datetime.now())
print(calendar.calendar(2023))
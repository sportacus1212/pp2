#1
from datetime import datetime, timedelta
now = datetime.now()
minusdays = now - timedelta(days=5)
print(now.strftime("%Y-%m-%d"))
print(minusdays.strftime("%Y-%m-%d"))

#2
from datetime import datetime, timedelta
now = datetime.now()
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)
print(yesterday.strftime("%Y-%m-%d"))
print(now.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))

#3
from datetime import datetime
current_d = datetime.now()
new_d = current_d.replace(microsecond=0)
print(current_d)
print(new_d)

#4
from datetime import datetime

# Get the two dates from the user
date1_str = input("(YYYY-MM-DD HH:MM:SS): ")
date2_str = input("(YYYY-MM-DD HH:MM:SS): ")
date_format = "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)
difference = abs((date2 - date1).total_seconds())
print(int(difference))



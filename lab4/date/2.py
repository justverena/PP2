
from datetime import *
today = date.today()
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print(yesterday)
print(today)
print(tomorrow)
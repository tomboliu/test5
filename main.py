from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Taipei')

local_time = datetime.now(tz)

print(f"Hello World, Now is {local_time.strftime('%Y-%m-%d %H:%M:%S')} in Asia/Taipei")
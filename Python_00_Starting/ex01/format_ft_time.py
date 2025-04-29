import time
import datetime

seconds_since_epoch = time.time()

print(f"Seconds since January 1, 1970: {seconds_since_epoch:.4f} or {seconds_since_epoch:.2e}")

dt = datetime.datetime.fromtimestamp(seconds_since_epoch)

formatted_date = dt.strftime("%b %d %Y")

print(formatted_date)


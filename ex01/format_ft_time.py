import time
import datetime


epoch_time = time.time()


formatted_epoch_time = f"Seconds since January 1, 1970: {epoch_time:.4f} or {epoch_time:.2e} in scientific notation"
current_time = datetime.datetime.now().strftime("%b %d %Y")

print(formatted_epoch_time)
print(current_time)
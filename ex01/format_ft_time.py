import time
import datetime

seconds = time.time()
current_date = datetime.datetime.now()

print(
    f"Seconds since January 1, 1970: {seconds:,.4f} "
    f"or {seconds:.2e} in scientific notation"
)
print(current_date.strftime("%b %d %Y"))

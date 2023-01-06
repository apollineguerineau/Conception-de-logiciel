from datetime import datetime
from dateutil import tz

h=datetime.now()
print(h.strftime('%H:%M:%S'))

UTC = tz.gettz("America/New_York")
print(h.astimezone(tz=UTC).strftime('%H:%M:%S'))

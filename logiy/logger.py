from datetime import datetime
from dateutil import tz
import sys, uuid

from_zone = tz.tzutc()
to_zone = tz.gettz("Asia/Singapore")

''' the log directory is relative from where you start your code '''
log_dir = "logs/"
log_file = "{}.log".format(uuid.uuid1())

def log(message=None):
    log_date = datetime.utcnow().replace(tzinfo=from_zone).astimezone(to_zone).strftime("%d/%m/%Y %H:%M")
    print "[{log_date}] {message}".format(log_date=log_date, message=message)
#end def
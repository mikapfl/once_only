"""Run a python script or function only once in a given time frame."""

import pickle
import logging
import datetime

__version__ = "0.1.0"

## Time-Keeping functions
class Once(object):
    """True only once in the given time interval. Do not instantiante directly, you
    have to keep every Once instance with a given timedelta unique!"""
    def __init__(self, timedelta):
        microseconds = (timedelta.days*24*60*60 + timedelta.seconds) * 1000 * 1000 + timedelta.microseconds
        filename = '/var/lib/genconfig/timestamp_%d' % microseconds
        try:
            with open(filename, 'rb') as fd:
                lasttime = pickle.load(fd)
        except IOError:
            logging.warning(f'No database for timedelta {timedelta} found, using 1.1.1970')
            lasttime = datetime.datetime.fromtimestamp(0)
        now = datetime.datetime.now()
        self._truth = (now - lasttime) >= timedelta
        if self._truth:
            with open(filename, 'wb') as fd:
                pickle.dump(now, fd)

    def __call__(self):
        return self

    def __bool__(self):
        return self._truth

once_weekly = Once(datetime.timedelta(7))
once_daily = Once(datetime.timedelta(1))
once_hourly = Once(datetime.timedelta(0, 60*60))

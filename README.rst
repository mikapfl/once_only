====
Once
====


.. image:: https://img.shields.io/pypi/v/once.svg
        :target: https://pypi.python.org/pypi/once

.. image:: https://readthedocs.org/projects/once/badge/?version=latest
        :target: https://once.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Run a python script or function only once in a given time frame.

If, for example, you have a script or service which might be called frequently, but you want to report errors only once daily to not annoy people too much, `once` is the library for you.

Quickstart
----------

Suppose you want your script to complain, but not more than once a day. `once.daily` is the tool you need::

    import once

    @once.daily
    def complain():
        print("This is not right!")

Now you can run `complain` as often as you want, from the same python script or from others, it will only be run at
most once a day, so that at least 24 hours are between two complaints.

If you want to complain more or less often, there are other variants:

=================  ==========
object             time delta
=================  ==========
`once.weekly`      1 week
`once.daily`       1 day
`once.hourly`      1 hour
`once.minutely`    1 minute
`once.Once()`      custom `datetime.timedelta`
=================  ==========

Advanced Usage
--------------

Instead of using a `once.Once` object as a decorator, you can also access it directly via the `check_ready()` and
`check_ready_trigger()` functions::

    import once
    import datetime

    once_every_two_hours = once.Once(datetime.timedelta(hours=2))

    if once_every_two_hours.check_ready():
        print("More than two hours have passed since last run!")

    if not_a_dry_run and once_every_two_hours.check_ready_trigger():
        print("More than two hours have passed since last run - triggering timer and running!")

Note that all instances of `once.Once` with the same time delta share the same timer, but those with different
time deltas don't share the timer. So, if you have never run anything before, this::

    import once
    import datetime

    @once.minutely
    def run_minutely():
        print("minutely")

    @once.hourly
    def run_hourly():
        print("hourly")

    @once.Once(datetime.timedelta(minutes=60))
    def run_every_60_minutes():
        print("60 minutes")

    run_minutely()
    run_hourly()
    run_every_60_minutes()

will print "minutely" and "hourly", but not "60 minutes", because 60 minutes is the same as one hour,
so the 60 minutes timer will already be triggered by `run_hourly` and `run_every_60_minutes` will not be
run.

Further documentation can be found at: https://once.readthedocs.io.

License
-------
Copyright 2022, Potsdam-Institut für Klimafolgenforschung e.V.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this
file except in compliance with the License. You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under
the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied. See the License for the specific language governing
permissions and limitations under the License.

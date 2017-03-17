# stdlib Imports
import datetime
import math
import time

# Twisted Imports
from twisted.internet import defer

# PythonCollector Imports
from ZenPacks.zenoss.PythonCollector.datasources.PythonDataSource import PythonDataSourcePlugin


class FakeData(PythonDataSourcePlugin):
    @classmethod
    def config_key(cls, datasource, context):
        return (
            context.device().id,
            datasource.getCycleTime(context),
            context.id,
            datasource.id,
            )

    def collect(self, config):
        data = self.new_data()
        now = time.time()

        for datasource in config.datasources:
            for point in datasource.points:
                dpname = "{}_{}".format(datasource.datasource, point.id)
                data["values"][datasource.component][dpname] = {
                    "ten": 10,
                    "twenty": 20,
                    "fifty": 50,
                    "hundred": 100,
                    "epoch": now,
                    "pct1day": getpercentofday(),
                    "cos1min": getcos(now / 60),
                    "cos5min": getcos(now / 300),
                    "cos10min": getcos(now / 600),
                    "cos1hour": getcos(now / 3600),
                    }.get(point.id, None)

        return defer.succeed(data)


def getcos(n):
    """Return cosine of n between 0-10 instead of 0.0 and 1.0."""
    return (math.cos(n * math.pi) * 10) + 10


def getpercentofday():
    """Return the percent of the way through the day (0-100)."""
    now = datetime.datetime.now()
    return (now.hour * 3600 + now.minute * 60 + now.second) / 864.0

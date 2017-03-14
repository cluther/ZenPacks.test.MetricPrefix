"""Model static set of components for testing."""

# Twisted Imports
from twisted.internet import defer

# Zenoss Imports
from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap, RelationshipMap


class MetricPrefix(PythonPlugin):
    def collect(self, device, log):
        log.info("%s: faking data for %s", self.name(), device.id)

        dpa_rm = RelationshipMap(relname="defaultPrefixAggregates")
        cpa_rm = RelationshipMap(relname="contextPrefixAggregates")
        mpa_rm = RelationshipMap(relname="mixedPrefixAggregates")
        dpc_rm = RelationshipMap(relname="defaultPrefixComponents")
        cpc_rm = RelationshipMap(relname="contextPrefixComponents")

        for dpa_idx in range(1, 3):
            dpa_rm.append(
                ObjectMap(
                    modname="ZenPacks.test.MetricPrefix.DefaultPrefixAggregate",
                    data={"id": "dpa-{}".format(dpa_idx)}))

            for dpc_idx in range(1, 3):
                dpc_rm.append(
                    ObjectMap(
                        modname="ZenPacks.test.MetricPrefix.DefaultPrefixComponent",
                        data={
                            "id": "dpa-{}-dpc-{}".format(dpa_idx, dpc_idx),
                            "set_basePrefixAggregate": "dpa-{}".format(dpa_idx)}))

        for cpa_idx in range(1, 3):
            cpa_rm.append(
                ObjectMap(
                    modname="ZenPacks.test.MetricPrefix.ContextPrefixAggregate",
                    data={"id": "cpa-{}".format(cpa_idx)}))

            for cpc_idx in range(1, 3):
                cpc_rm.append(
                    ObjectMap(
                        modname="ZenPacks.test.MetricPrefix.ContextPrefixComponent",
                        data={
                            "id": "cpa-{}-cpc-{}".format(cpa_idx, cpc_idx),
                            "set_basePrefixAggregate": "cpa-{}".format(cpa_idx)}))

        for mpa_idx in range(1, 3):
            mpa_rm.append(
                ObjectMap(
                    modname="ZenPacks.test.MetricPrefix.MixedPrefixAggregate",
                    data={"id": "mpa-{}".format(mpa_idx)}))

            for dpc_idx in range(1, 2):
                dpc_rm.append(
                    ObjectMap(
                        modname="ZenPacks.test.MetricPrefix.DefaultPrefixComponent",
                        data={
                            "id": "mpa-{}-dpc-{}".format(mpa_idx, dpc_idx),
                            "set_basePrefixAggregate": "mpa-{}".format(mpa_idx)}))

            for cpc_idx in range(1, 2):
                cpc_rm.append(
                    ObjectMap(
                        modname="ZenPacks.test.MetricPrefix.ContextPrefixComponent",
                        data={
                            "id": "mpa-{}-cpc-{}".format(mpa_idx, cpc_idx),
                            "set_basePrefixAggregate": "mpa-{}".format(mpa_idx)}))

        return defer.succeed([dpa_rm, cpa_rm, mpa_rm, dpc_rm, cpc_rm])

    def process(self, device, results, log):
        log.info("%s: processing data from %s", self.name(), device.id)
        return results

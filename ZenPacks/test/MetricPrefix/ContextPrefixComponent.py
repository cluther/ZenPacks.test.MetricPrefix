from . import schema


class ContextPrefixComponent(schema.ContextPrefixComponent):
    def contextMetric(self):
        return True

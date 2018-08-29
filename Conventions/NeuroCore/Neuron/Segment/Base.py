from Conventions.Parameters import Parameters


class BaseParameters(Parameters):

    @property
    def LocalConditions(self):
        return "localConditions"

    @property
    def IModel(self):
        return "iModel"

    @property
    def SegmentName(self):
        return "segmentName"

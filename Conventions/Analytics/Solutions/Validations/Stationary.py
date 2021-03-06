from Conventions.Analytics.Solutions.StationaryBase import StationaryBaseParameters


class StationaryParameters(StationaryBaseParameters):

    @property
    def Name(self):
        return "name"

    @property
    def Domain(self):
        return "domain"

    @property
    def Steps(self):
        return "steps"

    @property
    def Results(self):
        return "results"

    @property
    def Transient(self):
        return "transient"

    @property
    def Function(self):
        return "function"

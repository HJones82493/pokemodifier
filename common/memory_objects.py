class MemoryObject:
    """Class to hold all common data amongst anything from memory"""
    def __init__(self, name: str):
        self._name: str = name

    @property
    def name(self):
        return self._name
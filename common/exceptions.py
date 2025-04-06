"""Module to define custom exceptions to use for verbosity"""

class OverwriteException(Exception):
    """Exception when data is overwritten improperly

    When reading in new data, or opening a new file, there is a flag to overwrite
    anything existing. If this flag is not set properly, this exception will be raised
    """
    pass
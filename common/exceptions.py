"""Module to define custom exceptions to use for verbosity"""

class OverwriteError(Exception):
    """Exception when data is overwritten improperly

    When reading in new data, or opening a new file, there is a flag to overwrite
    anything existing. If this flag is not set properly, this exception will be raised
    """
    pass

class InvalidAddressError(Exception):
    """Exception when attempting to retrieve an address that's out of range"""
    pass
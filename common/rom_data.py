"""Module to define RomData super class

Not meant to be used on its own, but instead to be inherited by the various generations.
We can use this class to store address mapping data, original values, etc.
"""
from typing import List

from common.exceptions import InvalidAddressError

class RomData:
    """The superclass for ROM data"""
    def __init__(self):
        """Initializes the ROM Data class"""
        self._raw_data: bytes = b""
        self._address_map: dict = {}

    def get_byte(self, address: int) -> int:
        """Method to get the value at a given address in the data

        Args:
            address - The address of the data to retrieve

        Returns:
            A byte string with the given data

        Raises:
            InvalidAddressError - If the address is outside the range of the data
        """
        if address < 0 or address >= len(self._raw_data):
            raise InvalidAddressError(f"Address: {address} is outside of valid range")
        return self._raw_data[address]

    def get_bytes(self, start: int, end: int) -> List[int]:
        """Method to retrieve a number of bytes

        Args:
            start - The beginning of the address range to retrieve
            end - The end of the address range to retrieve

        Returns:
            A list of the data from addresses {start} to {end}

        Raises:
            InvalidAddressError - If the range is outside the scope of the data
        """
        if start < 0:
            raise InvalidAddressError("Invalid start address, must be greater than or equal to 0")
        if end > len(self._raw_data):
            raise InvalidAddressError("Invalid ending address, outside of range of data")

        ret_data = []
        for i in range(start, end + 1):
            ret_data.append(self._raw_data[i])
        return ret_data
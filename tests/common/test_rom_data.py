import os
import unittest

from common.rom_data import RomData
from common.exceptions import InvalidAddressError

class TestRomData(unittest.TestCase):
    def setUp(self):
        self.rom_path = os.path.join(os.environ.get("BASE_DIR"), "blue.gb")
        with open(self.rom_path, "rb") as fp:
            self.data = fp.read()

        self.rd = RomData(self.data, {})

    def test_get_byte_success(self):
        addr = 0x0146
        expected_result = self.data[addr]
        actual_result = self.rd.get_byte(addr)

        self.assertEqual(actual_result, expected_result)

    def test_get_byte_fail_out_of_range(self):
        self.assertRaises(InvalidAddressError, self.rd.get_byte, -1)
        self.assertRaises(InvalidAddressError, self.rd.get_byte, len(self.data) + 1)

    def test_get_bytes_success(self):
        start = 0x0134
        end = 0x0144
        expected_result = []
        for item in self.data[start:end + 1]:
            expected_result.append(item)
        actual_result = self.rd.get_bytes(start, end)

        self.assertEqual(actual_result, expected_result)

    def test_get_bytes_fail_out_of_range(self):
        start = -1
        end = len(self.data) + 1

        self.assertRaises(InvalidAddressError, self.rd.get_bytes, start, end)
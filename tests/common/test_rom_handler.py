import os
import unittest

from common.rom_handler import RomReader, RomWriter
from common.exceptions import InvalidAddressError

class TestRomReader(unittest.TestCase):
    def setUp(self):
        self.rom_path = os.path.join(os.environ.get("BASE_DIR"), "blue.gb")
        with open(self.rom_path, "rb") as fp:
            self.data = fp.read()

        self.rr = RomReader(self.rom_path, True)

    def test_rom_reader_create_success(self):
        expected_result = self.data
        actual_result = self.rr.file_data
        self.assertEqual(expected_result, actual_result)

class TestRomWriter(unittest.TestCase):
    def setUp(self):
        self.write_path = os.path.join(os.environ.get("BASE_DIR"), "blue.gb.tmp")
        self.rom_path = os.path.join(os.environ.get("BASE_DIR"), "blue.gb")
        with open(self.rom_path, "rb") as fp:
            self.data = fp.read()
        self.rw = RomWriter(self.data, self.write_path, False)

    def test_rom_write_success(self):
        self.assertFalse(os.path.exists(self.write_path))
        self.rw.write()
        self.assertTrue(os.path.exists(self.write_path))
        os.remove(self.write_path)
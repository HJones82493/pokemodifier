import os
import unittest

from common.character_encoding import CharacterDecoder
from gen_1.data.character_map import ENGLISH

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "..")

class TestCharacterDecoder(unittest.TestCase):
    def setUp(self):
        self.cd = CharacterDecoder(ENGLISH)

    def test_decode_character_success(self):
        expected_result = "A"
        actual_result = self.cd.decode_character(0x80)

        self.assertEqual(expected_result, actual_result)

    def test_decode_character_fail_out_of_range(self):
        self.assertRaises(OverflowError, self.cd.decode_character, 0x105)

    def test_decode_characters_success(self):
        expected_result = "MASTER BALL"
        data = [140, 128, 146, 147, 132, 145, 127, 129, 128, 139, 139]
        actual_result = self.cd.decode_characters(data)

        self.assertEqual(expected_result, actual_result)

    def test_decode_characters_fail_out_of_range(self):
        data = [140, 128, 146, 147, 132, 145, 127, 129, 128, 139, 139, 270]
        self.assertRaises(OverflowError, self.cd.decode_characters, data)
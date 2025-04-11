import os
import unittest

from common.character_encoding import CharacterEncoder
from gen_1.data.character_map import ENGLISH

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "..")

class TestCharacterEncoder(unittest.TestCase):
    def setUp(self):
        self.ce = CharacterEncoder(ENGLISH)

    def test_encode_character_success(self):
        expected_result = 0x80
        actual_result = self.ce.encode_character('A')

        self.assertEqual(expected_result, actual_result)

    def test_encode_character_fail_invalid_character(self):
        self.assertRaises(ValueError, self.ce.encode_character, "\n")

    def test_encode_string_success(self):
        expected_result = [140, 128, 146, 147, 132, 145, 127, 129, 128, 139, 139]
        actual_result = self.ce.encode_string("MASTER BALL")

        self.assertEqual(expected_result, actual_result)

    def test_encode_string_fail_invalid_character(self):
        self.assertRaises(ValueError, self.ce.encode_string, "Hello\n")
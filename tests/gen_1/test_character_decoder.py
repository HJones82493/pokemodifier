import sys

sys.path.append('.')
sys.path.append('..')

import pytest

from pokemodifier.gen_1.character_decoder import CharacterDecoder

def test_all_values_defined():
	cd = CharacterDecoder()
	try:
		for i in range(0x00, 0x100):
			_ = cd.decode_byte(i)
	except Exception as e:
		assert False, e


def test_decode_byte_expected_success():
	test_byte = 0x80
	expected_result = "A"

	cd = CharacterDecoder()
	actual_result = cd.decode_byte(test_byte)

	assert actual_result == expected_result


def test_decode_byte_expected_fail_value_out_of_range():
	cd = CharacterDecoder()
	with pytest.raises(IndexError):
		_ = cd.decode_byte(0x100)


def test_decode_byte_array_expected_success():
	test_array = [0x87, 0xA4, 0xAB, 0xAB, 0xAE]
	expected_result = "Hello"

	cd = CharacterDecoder()
	actual_result = cd.decode_byte_array(test_array)

	assert actual_result == expected_result


def test_decode_byte_array_expected_fail_wrong_characters():
	test_array = [0x87, 0xA4, 0xAB, 0xAB, 0xAE]
	expected_result = "World"

	cd = CharacterDecoder()
	actual_result = cd.decode_byte_array(test_array)

	assert actual_result != expected_result
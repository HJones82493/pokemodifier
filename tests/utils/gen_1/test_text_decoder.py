import pytest

from pokemodifier.utils.gen_1.text_decoder import TextDecoder

class TestEncoder:
	character_decoder = TextDecoder()

	def test_encoding_happy_path(self):
		expected_results = "Kaelthreast"
		values_to_decode = [138, 160, 164, 171, 179, 167, 177, 164, 160, 178, 179]

		results = self.character_decoder.decode_values(values_to_decode)

		assert results == expected_results

	def test_decoding_no_values(self):
		values_to_decode = []
		expected_results = ""

		results = self.character_decoder.decode_values(values_to_decode)

		assert results == expected_results

	def test_encoding_invalid_character(self):
		values_to_decode = [138, 160, 300]

		with pytest.raises(ValueError):
			self.character_decoder.decode_values(values_to_decode)
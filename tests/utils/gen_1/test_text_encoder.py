import pytest

from pokemodifier.utils.gen_1.text_encoder import TextEncoder

class TestEncoder:
	character_encoder = TextEncoder()

	def test_encoding_happy_path(self):
		string_to_encode = "Kaelthreast"
		expected_results = [138, 160, 164, 171, 179, 167, 177, 164, 160, 178, 179]

		results = self.character_encoder.encode_string(string_to_encode)

		assert results == expected_results

	def test_encoding_no_values(self):
		string_to_encode = ""
		expected_results = []

		results = self.character_encoder.encode_string(string_to_encode)

		assert results == expected_results

	def test_encoding_mismatch(self):
		string_to_encode = "Hello"
		expected_results = [1, 2, 3, 4, 5]

		results = self.character_encoder.encode_string(string_to_encode)

		assert results != expected_results

	def test_encoding_invalid_character(self):
		string_to_encode = "Hello{"

		with pytest.raises(Exception):
			self.character_encoder.encode_string(string_to_encode)
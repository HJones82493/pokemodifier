from typing import List

from pokemodifier.utils.gen_1.character_map import CharacterMap

class TextDecoder:
	def __init__(self):
		self._character_map = CharacterMap()

	def decode_values(self, values_to_decode: List[int]) -> str:
		"""Method to decode a list of encoded values

		This method is used to turn a list of encoded character values
		to an ascii string. 

		Parameters
			values_to_decode - A list of the hex/int values read from the ROM.

		Returns
			str - A valid ascii string based on the gen 1 charmap

		Raises
			ValueError - If a provided hex value does not map to an ascii character
		"""
		decoded_str = ""
		current_position = 0
		for value in values_to_decode:
			temp = self._character_map.character_from_hex(value)
			if not temp:
				raise ValueError(f"Invalid hex value provided at position {current_position}")

			decoded_str += temp
			current_position += 1
		return decoded_str
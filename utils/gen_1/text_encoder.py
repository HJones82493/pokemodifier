from typing import List

from pokemodifier.utils.gen_1.character_map import CharacterMap

class TextEncoder:
	def __init__(self):
		self._character_map = CharacterMap()

	def encode_string(self, string_to_encode: str) -> List[int]:
		"""Method to take a provided string and encode it
			
		This method is used to take an entire tring of ASCII characters
		and encode it into the encoding used by the gen 1 games. Will throw
		an exception if an illegal character is included in the string 

		Parameters 
			string_to_encode - The string to be encoded

		Returns
			List[int] - a list of the encoded string values

		Raises
			ValueError - If an ascii character is provided that does not have a valid
						 mapping in the gen 1 charset
		"""
		encoded_values = []
		current_position = 0
		for char in string_to_encode:
			temp = self._character_map.hex_from_character(char)

			if not temp:
				raise ValueError(f"Illegal character in string at position {str(current_position)}")
			encoded_values.append(temp)
			current_position += 1

		return encoded_values
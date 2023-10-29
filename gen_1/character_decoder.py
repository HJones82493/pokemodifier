from typing import List

class CharacterDecoder:
	def __init__(self):
		self._decoding_map = dict()
		self._setup_decoding_map()

	def decode_byte(self, encoded_byte: int) -> str:
		if encoded_byte not in range(0x00, 0x100):
			raise IndexError(f"Invalid byte: {encoded_byte}.\nOnly values from 0x00 - 0xFF can be decoded")
		return self._decoding_map[encoded_byte]

	def decode_byte_array(self, encoded_bytes: List[int]) -> str:
		ret_str = ""
		try:
			for byte in encoded_bytes:
				ret_str += self.decode_byte(byte)
		except IndexError as e:
			# This feels redundant, but will be used for logging later on
			raise
		return ret_str

	def _setup_decoding_map(self):
		# First we setup the characters that don't map. This includes
		# NULL, Map Tiles, and Control Characters
		for i in range(0x60):
			self._decoding_map[i] = ""

		# The letters mapped from 0x60 to 0x6C are bolded, but for decoding
		# purposes, we can simply display them as normal. 0x6E and 0x6F are
		# Kanji characters, but we're using utf-8.
		self._decoding_map[0x60] = "A"
		self._decoding_map[0x61] = "B"
		self._decoding_map[0x62] = "C"
		self._decoding_map[0x63] = "D"
		self._decoding_map[0x64] = "E"
		self._decoding_map[0x65] = "F"
		self._decoding_map[0x66] = "G"
		self._decoding_map[0x67] = "H"
		self._decoding_map[0x68] = "I"
		self._decoding_map[0x69] = "V"
		self._decoding_map[0x6A] = "S"
		self._decoding_map[0x6B] = "L"
		self._decoding_map[0x6C] = "M"
		self._decoding_map[0x6D] = ":"
		self._decoding_map[0x6E] = ""
		self._decoding_map[0x6F] = ""

		# The first 4 are just different directions of ' and ", we can substitute
		# the non-directional versions here
		self._decoding_map[0x70] = "'"
		self._decoding_map[0x71] = "'"
		self._decoding_map[0x72] = "\""
		self._decoding_map[0x73] = "\""

		# 0x74 - 0x7E are either Kanji or not supported by utf-8
		for i in range(0x74, 0x7F):
			self._decoding_map[i] = ""

		# 0x7F is the space character for the game
		self._decoding_map[0x7F] = " "

		# Next we get to the capital English letters
		letter = "A"
		for i in range(0x80, 0x9A):
			self._decoding_map[i] = letter
			letter = chr(ord(letter) + 1)

		# A few special characters
		self._decoding_map[0x9A] = "("
		self._decoding_map[0x9B] = ")"
		self._decoding_map[0x9C] = ":"
		self._decoding_map[0x9D] = ";"
		self._decoding_map[0x9E] = "["
		self._decoding_map[0x9F] = "]"

		# Lowercase English letters
		letter = "a"
		for i in range(0xA0, 0xBA):
			self._decoding_map[i] = letter
			letter = chr(ord(letter) + 1)

		self._decoding_map[0xBA] = ""
		self._decoding_map[0xBB] = "'d"
		self._decoding_map[0xBC] = "'l"
		self._decoding_map[0xBD] = "'s"
		self._decoding_map[0xBE] = "'t"
		self._decoding_map[0xBF] = "'v"

		# 0xC0 - 0xDF are intentionally blanks
		for i in range(0xC0, 0xE0):
			self._decoding_map[i] = ""

		self._decoding_map[0xE0] = "'"
		self._decoding_map[0xE1] = "PK"
		self._decoding_map[0xE2] = "MN"
		self._decoding_map[0xE3] = "-"
		self._decoding_map[0xE4] = "'r"
		self._decoding_map[0xE5] = "'m"
		self._decoding_map[0xE6] = "?"
		self._decoding_map[0xE7] = "!"
		self._decoding_map[0xE8] = "."
		# 0xE9 - 0xEE are special characters or directional arrows
		# 0xEF is the male symbol
		self._decoding_map[0xE9] = ""
		self._decoding_map[0xEA] = ""
		self._decoding_map[0xEB] = ""
		self._decoding_map[0xEC] = ""
		self._decoding_map[0xED] = ""
		self._decoding_map[0xEE] = ""
		self._decoding_map[0xEF] = "(M)"

		#0xF0 is the Pokedollar sign. $ is substituted to not lose meaning
		self._decoding_map[0xF0] = "$"
		self._decoding_map[0xF1] = ""
		self._decoding_map[0xF2] = "."
		self._decoding_map[0xF3] = "/"
		self._decoding_map[0xF4] = ","
		# 0xF0 is the female symbol
		self._decoding_map[0xF5] = "(F)"

		#Finally, the numbers
		number = "0"
		for i in range(0xF6, 0x100):
			self._decoding_map[i] = number
			number = chr(ord(number) + 1)
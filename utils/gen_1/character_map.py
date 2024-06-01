class CharacterMap:
	def __init__(self):
		self._characters = {}
		self._init_characters()

	def _init_characters(self):
		"""Method to initialize the character list

		This method is to setup the encoding and decoding charset for the game.
		Control characters, map tiles, and variable characters are not included 
		because they're not used in text based things that would need to be changed.
		These characters are mapped from 0x00-0x7E, the blanks from 0xC0 - 0xDF, and 
		a few other special characters at various other addresses

		Character map source: 
		https://bulbapedia.bulbagarden.net/wiki/Character_encoding_(Generation_I)#Variable_characters
		"""
		self._characters[0x7F] = " "
		# 65 is the ascii code for 'A'
		current_char = 65
		for i in range(0x80, 0x9A):
			self._characters[i] = chr(current_char)
			current_char += 1
		# A few non-letter characters
		self._characters[0x9A] = "("
		self._characters[0x9B] = ")"
		self._characters[0x9C] = ":"
		self._characters[0x9D] = ";"
		self._characters[0x9E] = "["
		self._characters[0x9F] = "]"

		# Lowercase letters, starts at ascii 97 which is 'a'
		current_char = 97
		for i in range(0xA0, 0xBA):
			self._characters[i] = chr(current_char)
			current_char += 1

		self._characters[0xE0] = "'"
		self._characters[0xE3] = "-"
		self._characters[0xE6] = "?"
		self._characters[0xE7] = "!"
		self._characters[0xE8] = "."
		self._characters[0xF3] = "/"
		self._characters[0xF4] = ","

		# We're saving the integers as chars for consistency
		current_char = 48
		for i in range(0xF6, 0x100):
			self._characters[i] = chr(current_char)
			current_char += 1

	def character_from_hex(self, hex_value: int) -> str:
		"""Method to return the character at a given hex value

		This method will provide the character that is represented by a given 
		hex value. Used primarily for decoding

		Parameters:
			hex_value - The hex value from the ROM, the encoded value

		Returns:
			str - The character represented in ascii
		"""
		if hex_value not in self._characters:
			return ""
		return self._characters[hex_value]

	def hex_from_character(self, ascii_char: str) -> int:
		"""Method to return the hex of a given character

		This method is basically the opposite of `character_from_hex`, returning
		the hex value of the ASCII character that was provided

		Parameters:
			ascii_char - The ascii char to retrieve the encoded hex value for

		Returns
			int - The hex value of the provided char
		"""
		if len(ascii_char) != 1:
			raise Exception("Invalid argument. Please provide single character")
		for k, v in self._characters.items():
			if v == ascii_char:
				return k
		return ""
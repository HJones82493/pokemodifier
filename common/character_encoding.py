from typing import List, Dict

from gen_1.data.character_map import ENGLISH, JAPANESE

LANGUAGE_MAPPING: Dict[str, Dict] = {
    "en": ENGLISH,
    "ja": JAPANESE
}
ENCODING: str = "utf16"

class CharacterDecoder:
    """Class used to handle character decoding

    Since Generation 1 uses a non-ascii encoding of the character values, we need
    a way to translate that back and forth. Currently, the only supported languages
    are English and Japanese.

    WARNING: Attempting to use a language other than the one the cartridge/ROM was made
    for will cause weird/strange results and/or corruption. You have been warned
    """
    def __init__(self, language_map: Dict[int, bytes]):
        """Initializes the decoder

        Args:
            language - The 2-letter code of the language to use.
                Currently only supports English (en) and Japanese (ja)
        """
        self._map: Dict[int, bytes] = language_map

    def decode_character(self, character: int) -> str:
        """Method to decode a character read from the ROM

        Args:
            character - The encoded character read from ROM

        Returns:
            A readable string of the encoded character

        Raises:
            OverflowError - If a character int is supplied that is out of range
        """
        if character >= 0x100:
            raise OverflowError("Encoded character too large, must be in range 0x00-0xFF (inclusive)")
        return self._map.get(character).decode(ENCODING)

    def decode_characters(self, characters: List[int]) -> str:
        """Method to decode multiple characters at once

        Args:
            characters - A list of encoded characters read from ROM

        Returns:
            A readable string of the encoded characters

        Raises:
            OverflowError - If any of the characters are out of range
        """
        ret_str: str = ""
        for character in characters:
            ret_str += self.decode_character(character)
        return ret_str


class CharacterEncoder:
    """Class to encode ascii / printable characters to ROM codes

    Since Generation 1 uses a non-ascii encoding of the character values, we need
    a way to translate that back and forth. Currently, the only supported languages
    are English and Japanese.

    WARNING: Attempting to use a language other than the one the cartridge/ROM was made
    for will cause weird/strange results and/or corruption. You have been warned
    """
    def __init__(self, language_map: Dict[int, bytes]):
        """Initializes the Character Encoder

        Args:
            language - The 2-letter code of the language to use.
                Currently only supports English (en) and Japanese (ja)
        """
        self._map = language_map

    def encode_character(self, character: str) -> int:
        """Method to translate printable / ascii characters into ROM value

        Args:
            character - The character to encode

        Returns:
            The integer value to write to ROM

        Raises:
            ValueError - If the character is not supported
                         If more than 1 character is provided
        """
        if len(character) != 1:
            raise ValueError("Please supply only a single character")
        enc_char = character.encode(ENCODING)
        if enc_char not in self._map.values():
            raise ValueError("Unsupported character")

        for k, v in self._map.items():
            if v == enc_char:
                return k

    def encode_string(self, string: str) -> List[int]:
        """Method to encode an entire string

        Args:
            string - The character string to encode

        Returns:
            A list of values to write to ROM

        Raises:
            ValueError - If any of the characters are not supported
        """
        ret_data = []
        for c in string:
            ret_data.append(self.encode_character(c))
        return ret_data
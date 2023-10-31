import os

from typing import List

BASE_PATH = os.path.join(
				os.path.dirname(
					os.path.realpath(__file__)
				),
				".."
			)

SUPPORTED_GENERATIONS = [1]
# Since this is historical and static data, we can hard code it instead of using some kind
# of config file
GENERATION_MAP = {
	"red"			: 1,
	"blue" 			: 1,
	"yellow"		: 1,
	"gold"			: 2,
	"silver"		: 2,
	"crystal" 		: 2,
	"ruby"			: 3,
	"sapphire"		: 3,
	"emerald"		: 3,
	"diamond"		: 4,
	"pearl"			: 4,
	"platinum"		: 4,
	"black"			: 5,
	"white"			: 5,
	"black_2"		: 5,
	"white_2"		: 5,
	"x"				: 6,
	"y"				: 6,
	"sun"			: 7,
	"moon"			: 7,
	"ultra_sun"		: 7,
	"ultra_moon"	: 7,
	"sword"			: 8,
	"shield"		: 8,
	"scarlet"		: 9,
	"violet"		: 9
}

class ROMHandler:
	def __init__(self, game_nae: str):
		self.game_name = game_name.lower()

		self._set_generation()
		self.fp = self._open_base_rom()
		self.fw = self._open_modified_rom()

	def read_data(self, number_of_bytes: int, offset: int = -1) -> List[int]:
		if not self.fp:
			raise IOError("ROM has either been closed or never opened")
		if offset >= 0:
			self.fp.seek(offset)
		temp_data = fp.read(number_of_bytes)
		if len(temp_data) < number_of_bytes:
			raise ValueError("Attempted to read more bytes than available")

		return [char for char in temp_data]

	def write_data(self, data: List[int], offset: int) -> None:
		pass

	def _set_generation(self):
		if self.game_name not in GENERATION_MAP:
			raise ValueError(f"Invalid game name provided: {self.game_name}")
		self.generation = GENERATION_MAP.get(self.game_name)

	def _open_base_rom(self):
		roms_path = os.path.join(
			BASE_PATH,
			f"gen_{self.generation}",
			"base_roms"
		)
		file_ext = "null"
		if self.generation == 1:
			file_ext = "gb"
		elif self.generation == 2:
			file_ext = "gbc"
		elif self.generation == 3:
			file_ext = "gba"
		elif self.generation == 4:
			file_ext = "nds"

		file_fqdn = os.path.join(roms_path, f"{self.game_name}.{file_ext}")
		try:
			self.fp = open(file_fqdn, 'rb')
		except IOError as io_e:
			# Do something with logging, although this should never happen
			raise

	def _open_modified_rom(self):
		# Need to figure out file structure for writing roms, especially assuming this will
		# be used at scale. For now, leaving this blank
		pass
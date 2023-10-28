class RomMap:
	SHOP_START_VALUE = 0xFE
	SHOP_END_VALUE = 0xFF
	self._addresses = dict()
	def __init__(self):
		self._setup_rom_map()

	def _setup_rom_map(self):
		self._addresses["shops"] = {"start": 0x2442, "end": 0x24D5, "size": 0}
		self._addresses["item_prices"] = {"start": 0x4608, "end": 0x472A, "size": 2}
from items import ItemInfo

class RomMap:
	SHOP_START_VALUE = 0xFE
	SHOP_END_VALUE = 0xFF
	self._addresses = dict()
	def __init__(self):
		self._setup_rom_map()

	def _setup_rom_map(self):
		self._addresses["shops"] = {"start": 0x2442, "end": 0x24D5, "size": 0}
		self._addresses["item_prices"] = {"start": 0x4608, "end": 0x472A, "size": 2}

	def get_item_price_address(self, item_name: str) -> int:
		i = ItemInfo()
		try:
			item_index = i.get_item_index(item_name)
		except ValueError as e:
			raise e

		item_size = self._addresses.get("item_prices").get("size")
		item_start = self._addresses.get("item_prices").get("start")
		return item_start + (item_index * item_size)

	def get_item_shop_range(self) -> tuple[int, int]:
		return (
			self._addresses.get("shops").get("start"),
			self._addresses.get("shops").get("end")
		)
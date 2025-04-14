from common.memory_objects import MemoryObject
from gen_1.data.map_data import ITEM_MAP


class Item(MemoryObject):
    """Representation of all the data for an item in ROM"""
    PRICE_SIZE = 3
    PRICE_LEN = 6

    def __init__(self, name: str):
        """Initializes an item object

        NOTE: This uses the default names of items. If an item was changed and written
        to ROM, it is still going to be referenced by its original name

        Args:
            name - The name of the item

        Raises:
            NameError - If an invalid name is supplied
        """
        super().__init__(name)
        u_name = name.upper()
        self._id = ITEM_MAP.get("ids").get(u_name, None)
        self._price = 0
        if not self._id:
            raise NameError(f"{name} is an invalid name")
        self._name_address = ITEM_MAP.get("names").get(u_name)
        self._name_length = self._name_address.get("end") - self._name_address.get("start")
        self._price_address = ITEM_MAP.get("prices").get(u_name)

    @property
    def name_address(self):
        return [self._name_address.get("start"), self._name_address.get("end")]

    @property
    def price_address(self):
        return [self._price_address, self._price_address + self.PRICE_SIZE]

    @property
    def item_id(self):
        return self._id

    @property
    def price(self):
        price_str = str(self._price).zfill(self.PRICE_LEN)
        return [int(price_str[:2]), int(price_str[2:4]), int(price_str[4:])]

    @property
    def padding(self):
        return self._name_length - len(self._name)


    def change_name(self, new_name: str):
        """Method to change the stored name of an item

        Args:
            new_name - The name to change the item to

        Raises:
              NameError - If the new name is too long to fit
        """
        if len(new_name) > self._name_length:
            raise IndexError(f"New name is too long, it must be between 1 and {self._name_length} characters")
        self._name = new_name

    def change_price(self, new_price: int):
        """Method to change the stored price of the item

        Args:
            new_price - The new price to set the item to

        Raises:
            ValueError - If a price is specified below 0 or above 999999
        """
        if new_price not in range(0, 1000000):
            raise ValueError("Price must be in the range 0-999999")
        self._price = new_price

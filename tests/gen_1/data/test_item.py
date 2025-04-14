import unittest

from gen_1.data.item import Item

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item("Master Ball")

    def test_item_name_change_success(self):
        expected_value = "Ball Master"

        self.item.change_name("Ball Master")

        self.assertEqual(expected_value, self.item.name)

    def test_item_name_change_fail_too_long(self):
        self.assertRaises(IndexError, self.item.change_name, "Some data that's way too long")

    def test_item_name_padding_success(self):
        expected_value = 2
        self.item.change_name("Some Data")


        self.assertEqual(expected_value, self.item.padding)

    def test_item_change_price_success(self):
        expected_value = [0, 2, 0]
        self.item.change_price(200)

        self.assertEqual(expected_value, self.item.price)

    def test_item_change_price_fail_out_of_range(self):
        self.assertRaises(ValueError, self.item.change_price, 1000000)


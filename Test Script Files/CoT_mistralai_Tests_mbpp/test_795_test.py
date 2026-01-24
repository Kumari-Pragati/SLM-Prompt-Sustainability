import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(cheap_items([], 1), [])

    def test_single_item(self):
        item = {'price': 10}
        self.assertListEqual(cheap_items([item], 1), [item])

    def test_multiple_items_one_cheapest(self):
        item1 = {'price': 10}
        item2 = {'price': 11}
        self.assertListEqual(cheap_items([item1, item2], 1), [item1])

    def test_multiple_items_multiple_cheapest(self):
        item1 = {'price': 10}
        item2 = {'price': 10}
        self.assertListEqual(cheap_items([item1, item2], 2), [item1, item2])

    def test_multiple_items_more_than_n(self):
        item1 = {'price': 10}
        item2 = {'price': 11}
        item3 = {'price': 12}
        self.assertListEqual(cheap_items([item1, item2, item3], 2), [item1, item2])

    def test_invalid_input_negative_n(self):
        with self.assertRaises(ValueError):
            cheap_items([{'price': 10}], -1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            cheap_items('not a list', 1)

    def test_invalid_input_no_price(self):
        with self.assertRaises(TypeError):
            cheap_items([{'not_a_price': 10}], 1)

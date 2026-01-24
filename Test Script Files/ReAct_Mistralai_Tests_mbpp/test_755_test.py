import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

    def test_single_item_list(self):
        self.assertIsNone(second_smallest([1]))

    def test_two_identical_items_list(self):
        self.assertIsNone(second_smallest([1, 1]))

    def test_two_unique_items_list(self):
        self.assertEqual(second_smallest([1, 2]), 1)

    def test_three_unique_items_list(self):
        self.assertEqual(second_smallest([1, 2, 3]), 2)

    def test_four_unique_items_list(self):
        self.assertEqual(second_smallest([1, 2, 3, 4]), 2)

    def test_five_unique_items_list(self):
        self.assertEqual(second_smallest([1, 2, 3, 4, 5]), 3)

    def test_large_list(self):
        large_list = [i for i in range(100)]
        self.assertEqual(second_smallest(large_list), large_list[1])

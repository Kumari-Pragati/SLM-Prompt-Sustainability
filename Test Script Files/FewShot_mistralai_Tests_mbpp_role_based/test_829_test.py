import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 5]), 4)

    def test_single_element(self):
        self.assertEqual(second_frequent([1]), None)

    def test_two_elements(self):
        self.assertEqual(second_frequent([1, 2]), None)

    def test_multiple_unique_elements(self):
        self.assertEqual(second_frequent([1, 2, 3, 4, 5]), None)

    def test_empty_list(self):
        self.assertEqual(second_frequent([]), None)

    def test_list_with_only_one_value(self):
        self.assertEqual(second_frequent([10]), 10)

    def test_list_with_multiple_same_values(self):
        self.assertEqual(second_frequent([1, 1, 2, 2, 3]), 3)

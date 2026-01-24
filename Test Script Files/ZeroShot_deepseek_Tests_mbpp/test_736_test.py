import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(left_insertion([], 5), 0)

    def test_existing_element(self):
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 3), 2)

    def test_new_element(self):
        self.assertEqual(left_insertion([1, 2, 4, 5], 3), 2)

    def test_duplicate_elements(self):
        self.assertEqual(left_insertion([1, 2, 2, 4, 5], 2), 1)

    def test_negative_numbers(self):
        self.assertEqual(left_insertion([-5, -3, 0, 2, 4], -4), 1)

    def test_large_numbers(self):
        self.assertEqual(left_insertion([100, 200, 300, 400, 500], 250), 2)

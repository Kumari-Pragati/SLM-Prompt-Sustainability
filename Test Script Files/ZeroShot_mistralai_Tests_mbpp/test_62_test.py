import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(smallest_num([]))

    def test_single_element(self):
        self.assertEqual(smallest_num([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(smallest_num([4, 2, 5, 1, 3]), 1)

    def test_negative_numbers(self):
        self.assertEqual(smallest_num([-2, -4, -1, 0]), -4)

    def test_floats(self):
        self.assertAlmostEqual(smallest_num([1.5, 2.2, 0.1]), 0.1)

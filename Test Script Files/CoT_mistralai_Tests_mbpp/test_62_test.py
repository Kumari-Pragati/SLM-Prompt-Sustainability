import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(smallest_num([]))

    def test_single_element(self):
        self.assertEqual(smallest_num([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(smallest_num([3, 1, 4, 1, 5, 9, 2, 4, 2]), 1)

    def test_negative_numbers(self):
        self.assertEqual(smallest_num([-3, -1, 0, 2]), -3)

    def test_floats(self):
        self.assertAlmostEqual(smallest_num([3.14, 2.71, 1.618]), 1.618)

    def test_mixed_types(self):
        self.assertRaises(TypeError, smallest_num, [1, 2, "three", 4])

    def test_duplicates(self):
        self.assertEqual(smallest_num([1, 1, 2, 3, 4]), 1)

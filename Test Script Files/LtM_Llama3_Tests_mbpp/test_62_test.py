import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(smallest_num([1, 2, 3]), 1)
        self.assertEqual(smallest_num([-1, 0, 1]), -1)
        self.assertEqual(smallest_num([5, 5, 5]), 5)

    def test_empty_input(self):
        self.assertRaises(ValueError, smallest_num, [])

    def test_single_element(self):
        self.assertEqual(smallest_num([1]), 1)

    def test_multiple_min_values(self):
        self.assertEqual(smallest_num([-1, -2, -3]), -3)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            smallest_num(['a', 'b', 'c'])

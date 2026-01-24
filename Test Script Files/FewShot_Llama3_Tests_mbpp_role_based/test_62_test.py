import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(smallest_num([1, 2, 3, 4, 5]), 1)

    def test_empty_list(self):
        self.assertRaises( ValueError, smallest_num, [])

    def test_single_element_list(self):
        self.assertEqual(smallest_num([10]), 10)

    def test_multiple_minima(self):
        self.assertEqual(smallest_num([-3, -2, -1, 0, 1]), -3)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            smallest_num(['a', 'b', 'c'])

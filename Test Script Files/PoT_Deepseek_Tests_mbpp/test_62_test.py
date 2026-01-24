import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(smallest_num([5, 3, 9, 1]), 1)

    def test_single_element(self):
        self.assertEqual(smallest_num([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(smallest_num([-5, -3, -9, -1]), -9)

    def test_duplicate_smallest(self):
        self.assertEqual(smallest_num([5, 3, 9, 1, 1]), 1)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            smallest_num([])

    def test_large_numbers(self):
        self.assertEqual(smallest_num([10**6, 10**7, 10**8]), 10**6)

    def test_float_numbers(self):
        self.assertEqual(smallest_num([5.5, 3.3, 9.9, 1.1]), 1.1)

import unittest
from mbpp_865_code import ntimes_list

class TestNTimesList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(ntimes_list([], 5), [])

    def test_single_element_list(self):
        self.assertEqual(ntimes_list([1], 5), [5])

    def test_multiple_element_list(self):
        self.assertEqual(ntimes_list([1, 2, 3], 5), [5, 10, 15])

    def test_negative_multiplier(self):
        self.assertEqual(ntimes_list([-1, 2, 3], 5), [-5, 10, 15])

    def test_zero_multiplier(self):
        self.assertEqual(ntimes_list([1, 2, 3], 0), [])

    def test_non_integer_multiplier(self):
        self.assertEqual(ntimes_list([1, 2, 3], 4.5), [4.5, 9, 13.5])

    def test_mixed_types_list(self):
        self.assertEqual(ntimes_list([1, 'a', 3.5], 5), [5, 'a', 17.5])

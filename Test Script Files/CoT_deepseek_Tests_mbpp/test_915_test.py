import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rearrange_numbs([0, 1, 2, 3, 4]), [0, 4, 3, 2, 1])

    def test_with_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3, 0, 1]), [0, -1, 1, -2, -3])

    def test_with_duplicates(self):
        self.assertEqual(rearrange_numbs([0, 2, 2, 3, 4]), [0, 4, 3, 2, 2])

    def test_with_large_numbers(self):
        self.assertEqual(rearrange_numbs([0, 100, 200, 300, 400]), [0, 400, 300, 200, 100])

    def test_with_zero_only(self):
        self.assertEqual(rearrange_numbs([0]), [0])

    def test_with_single_non_zero_number(self):
        self.assertEqual(rearrange_numbs([1]), [1])

    def test_with_empty_list(self):
        self.assertEqual(rearrange_numbs([]), [])

    def test_with_non_integer_values(self):
        with self.assertRaises(TypeError):
            rearrange_numbs([0, '1', 2, 3, 4])

    def test_with_none_values(self):
        with self.assertRaises(TypeError):
            rearrange_numbs([0, None, 2, 3, 4])

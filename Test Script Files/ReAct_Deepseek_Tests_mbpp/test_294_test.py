import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_val([]))

    def test_single_element(self):
        self.assertEqual(max_val([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)

    def test_mixed_types(self):
        self.assertEqual(max_val([1, '2', 3.0, 4, '5']), 4)

    def test_non_integer_elements(self):
        self.assertEqual(max_val(['1', 2, '3', 4, '5']), 5)

    def test_duplicates(self):
        self.assertEqual(max_val([5, 5, 5, 5]), 5)

    def test_mixed_integer_types(self):
        self.assertEqual(max_val([1, 2, 3, 4, float('inf')]), float('inf'))

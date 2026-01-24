import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(min_val([5, 3, 9, 1]), 1)

    def test_with_negative_numbers(self):
        self.assertEqual(min_val([5, -3, 9, -1]), -3)

    def test_with_mixed_types(self):
        self.assertEqual(min_val([5, '3', 9, 1]), 1)

    def test_with_non_integer_values(self):
        self.assertEqual(min_val(['5', '3', '9', '1']), '1')

    def test_with_empty_list(self):
        with self.assertRaises(ValueError):
            min_val([])

    def test_with_single_element(self):
        self.assertEqual(min_val([5]), 5)

    def test_with_all_same_elements(self):
        self.assertEqual(min_val([3, 3, 3]), 3)

    def test_with_float_numbers(self):
        self.assertEqual(min_val([5.5, 3.3, 9.9, 1.1]), 1.1)

    def test_with_large_numbers(self):
        self.assertEqual(min_val([10**10, 9*10**9, 8*10**8, 7*10**7]), 7*10**7)

    def test_with_non_integer_min(self):
        self.assertEqual(min_val([5, 3, 9, 1]), 1)

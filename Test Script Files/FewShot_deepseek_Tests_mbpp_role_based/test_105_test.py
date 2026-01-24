import unittest
from mbpp_105_code import count

class TestCount(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count([1, 2, 3, 4, 5]), 15)

    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(count([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(count([1, -1, 2, -2]), 0)

    def test_large_numbers(self):
        self.assertEqual(count(list(range(1, 10001))), 50005000)

    def test_float_numbers(self):
        self.assertAlmostEqual(count([1.1, 2.2, 3.3]), 6.6)

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            count([1, 'a', 2])

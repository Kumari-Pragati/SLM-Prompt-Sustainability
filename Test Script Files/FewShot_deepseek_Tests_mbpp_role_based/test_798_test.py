import unittest
from mbpp_798_code import _sum

class TestSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)

    def test_empty_list(self):
        self.assertEqual(_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(_sum([10]), 10)

    def test_negative_numbers(self):
        self.assertEqual(_sum([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(_sum([1, -2, 3, -4, 5]), 3)

    def test_large_numbers(self):
        self.assertEqual(_sum(list(range(1, 10001))), 50005000)

    def test_float_numbers(self):
        self.assertAlmostEqual(_sum([1.1, 2.2, 3.3]), 6.6)

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            _sum([1, 'two', 3])

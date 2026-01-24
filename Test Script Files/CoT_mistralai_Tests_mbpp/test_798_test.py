import unittest
from mbpp_798_code import _sum

class TestSumFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(_sum([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(_sum([1, -2, 3, -4, 5]), 6)

    def test_mixed_numbers(self):
        self.assertEqual(_sum([1, -2.5, 3, -4, 5]), 2.5)

    def test_float_numbers(self):
        self.assertAlmostEqual(_sum([1.1, 2.2, 3.3]), 6.6)

    def test_list_with_zero(self):
        self.assertEqual(_sum([0, 1, 2, 3, 4]), 10)

    def test_list_with_duplicates(self):
        self.assertEqual(_sum([1, 1, 1, 2, 3]), 7)

    def test_list_with_large_numbers(self):
        self.assertEqual(_sum([1000000001, 1000000002, 1000000003]), 3000000006)

    def test_list_with_small_numbers(self):
        self.assertEqual(_sum([-1000000001, -1000000002, -1000000003]), -3000000006)

    def test_list_with_string(self):
        with self.assertRaises(TypeError):
            _sum(['a', 'b', 'c'])

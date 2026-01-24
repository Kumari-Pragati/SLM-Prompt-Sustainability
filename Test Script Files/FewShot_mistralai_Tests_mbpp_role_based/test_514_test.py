import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)

    def test_negative_numbers(self):
        self.assertEqual(sum_elements((-1, -2, -3)), -6)

    def test_mixed_numbers(self):
        self.assertEqual(sum_elements((1, -2, 3)), 2)

    def test_empty_list(self):
        self.assertEqual(sum_elements([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_elements((4,)), 4)

    def test_large_numbers(self):
        self.assertEqual(sum_elements((1000000, 2000000, 3000000)), 6000000)

    def test_floats(self):
        self.assertAlmostEqual(sum_elements((1.1, 2.2, 3.3)), 6.6)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            sum_elements(('a', 'b', 'c'))

import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):
    def test_typical_input(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5]), 3.0)

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            Average([])

    def test_single_element_list(self):
        self.assertEqual(Average([1]), 1)

    def test_float_input(self):
        self.assertAlmostEqual(Average([1.0, 2.0, 3.0, 4.0, 5.0]), 3.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(Average([-1, -2, -3, -4, -5]), -3.0)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            Average([1, 2, 'a', 4, 5])

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            Average([1, 2, 3, 'a', 5])

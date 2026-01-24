import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):
    def test_empty_list(self):
        self.assertAlmostEqual(Average([]), 0)

    def test_single_element_list(self):
        self.assertAlmostEqual(Average([1]), 1)

    def test_positive_numbers(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5]), 3)

    def test_negative_numbers(self):
        self.assertAlmostEqual(Average([-1, -2, -3, -4, -5]), 1.25)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(Average([1, -2, 3, -4, 5]), 1.5)

    def test_floats(self):
        self.assertAlmostEqual(Average([1.1, 2.2, 3.3]), 2.2)

    def test_large_list(self):
        large_list = [i for i in range(1000)]
        self.assertAlmostEqual(Average(large_list), 500)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Average('string')

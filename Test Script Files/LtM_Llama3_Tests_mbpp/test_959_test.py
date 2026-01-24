import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):
    def test_simple_average(self):
        self.assertEqual(Average([1, 2, 3, 4, 5]), 3)

    def test_average_with_zero(self):
        self.assertEqual(Average([0, 1, 2, 3, 4]), 2)

    def test_average_with_negative(self):
        self.assertEqual(Average([-1, 0, 1, 2, 3]), 1)

    def test_average_with_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            Average([])

    def test_average_with_single_element(self):
        self.assertEqual(Average([5]), 5)

    def test_average_with_float(self):
        self.assertAlmostEqual(Average([1.0, 2.0, 3.0, 4.0, 5.0]), 3)

    def test_average_with_mixed_types(self):
        with self.assertRaises(TypeError):
            Average([1, 2, '3', 4, 5])

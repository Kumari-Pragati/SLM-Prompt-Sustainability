import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            Average([])

    def test_single_element_list(self):
        self.assertEqual(Average([1]), 1.0)

    def test_multiple_elements_list(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5]), 3.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(Average([1, -2, 3, -4, 5]), 1.5)

    def test_floating_point_numbers(self):
        self.assertAlmostEqual(Average([1.1, 2.2, 3.3, 4.4, 5.5]), 3.3)

import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(avg_calc([]), 0.0)

    def test_single_element_list(self):
        self.assertEqual(avg_calc([1]), 1.0)

    def test_multiple_elements_list(self):
        self.assertEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)

    def test_negative_numbers(self):
        self.assertEqual(avg_calc([1, -2, 3, -4, 5]), 1.0)

    def test_floats(self):
        self.assertEqual(avg_calc([1.0, 2.0, 3.0]), 2.0)

    def test_large_numbers(self):
        self.assertEqual(avg_calc([1000000000, 2000000000, 3000000000]), 2000000000.0)

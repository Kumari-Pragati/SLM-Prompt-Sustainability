import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvenNumbers(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(filter_evennumbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_empty_input(self):
        self.assertEqual(filter_evennumbers([]), [])

    def test_single_input(self):
        self.assertEqual(filter_evennumbers([0]), [0])

    def test_negative_input(self):
        self.assertEqual(filter_evennumbers([-1, -2, -3]), [-2, -4])

    def test_mixed_input(self):
        self.assertEqual(filter_evennumbers([1, 2, 3, 4, 5, 6, 7, 8]), [2, 4, 6, 8])

    def test_large_input(self):
        self.assertEqual(filter_evennumbers(list(range(100))), list(range(0, 100, 2)))

    def test_float_input(self):
        self.assertEqual(filter_evennumbers([1.5, 2.0, 3.5]), [2.0])

    def test_invalid_input(self):
        self.assertRaises(TypeError, filter_evennumbers, "not a list")

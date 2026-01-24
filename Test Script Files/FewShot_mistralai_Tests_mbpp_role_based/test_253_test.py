import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_integers(self):
        self.assertEqual(count_integer([-1, -2, -3, -4, -5]), 5)

    def test_zero(self):
        self.assertEqual(count_integer([0]), 1)

    def test_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_mixed_data_types(self):
        self.assertEqual(count_integer([1, 'a', 2, 'b', 3]), 3)

    def test_floats(self):
        self.assertEqual(count_integer([1.0, 2.0, 3.0]), 3)

    def test_strings(self):
        self.assertEqual(count_integer(['1', '2', '3']), 0)

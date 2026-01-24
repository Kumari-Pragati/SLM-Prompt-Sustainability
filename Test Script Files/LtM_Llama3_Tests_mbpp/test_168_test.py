import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(frequency([1, 2, 3, 4, 5], 3), 1)
        self.assertEqual(frequency([1, 2, 3, 4, 5], 1), 1)
        self.assertEqual(frequency([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(frequency([1, 2, 3, 4, 5], 6), 0)

    def test_empty_list(self):
        self.assertEqual(frequency([], 1), 0)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            frequency("abc", 1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            frequency([1, 2, 3, 4, 5], "a")

    def test_edge_cases(self):
        self.assertEqual(frequency([1, 1, 1, 1, 1], 1), 5)
        self.assertEqual(frequency([1, 2, 3, 4, 5], 2.5), 1)
        self.assertEqual(frequency([1, 2, 3, 4, 5], 0), 0)

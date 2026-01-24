import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(frequency([1, 2, 3, 4, 5], 3), 1)

    def test_edge(self):
        self.assertEqual(frequency([], 0), 0)
        self.assertEqual(frequency([1], 1), 1)
        self.assertEqual(frequency([1, 2, 3, 4, 5], 5), 1)

    def test_corner(self):
        self.assertEqual(frequency([1, 2, 3, 4, 5], 6), 0)
        self.assertEqual(frequency([1, 2, 3, 4, 5], 1), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            frequency(None, 1)
        with self.assertRaises(TypeError):
            frequency([1, 2, 3, 4, 5], None)

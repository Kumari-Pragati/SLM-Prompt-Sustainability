import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(frequency([1, 2, 3, 2, 4, 2, 5], 2), 3)

    def test_edge(self):
        self.assertEqual(frequency([], 1), 0)
        self.assertEqual(frequency([1], 1), 1)
        self.assertEqual(frequency([1, 2, 3], 1), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            frequency(None, 1)
        with self.assertRaises(TypeError):
            frequency([1, 2, 3], None)

    def test_edge_invalid_input(self):
        with self.assertRaises(TypeError):
            frequency(None, None)

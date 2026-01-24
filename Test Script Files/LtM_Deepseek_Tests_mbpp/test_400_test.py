import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(extract_freq([[1, 2, 3], [3, 2, 1]]), 1)
        self.assertEqual(extract_freq([[1, 2, 3], [1, 2, 3]]), 1)
        self.assertEqual(extract_freq([[1, 2, 3], [4, 5, 6]]), 2)

    def test_edge_conditions(self):
        self.assertEqual(extract_freq([]), 0)
        self.assertEqual(extract_freq([[]]), 1)
        self.assertEqual(extract_freq([[], []]), 1)

    def test_complex_cases(self):
        self.assertEqual(extract_freq([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), 1)
        self.assertEqual(extract_freq([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 3)
        self.assertEqual(extract_freq([[1, 2, 3], [1, 2, 3], [4, 5, 6]]), 2)

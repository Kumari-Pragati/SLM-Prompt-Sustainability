import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(extract_freq([(1, 2), (2, 1), (1, 1)]), 2)
        self.assertEqual(extract_freq([(3, 4), (4, 3)]), 1)
        self.assertEqual(extract_freq([(1, 1), (2, 2), (3, 3)]), 1)

    def test_edge_cases(self):
        self.assertEqual(extract_freq([(1, 1)]), 1)
        self.assertEqual(extract_freq([(1, 2), (1, 2)]), 1)
        self.assertEqual(extract_freq([(1, 2), (2, 1), (1, 2), (2, 1)]), 1)
        self.assertEqual(extract_freq([(1, 2), (2, 1), (1, 2), (2, 1), (1, 2)]), 1)

    def test_complex_cases(self):
        self.assertEqual(extract_freq([(1, 2), (2, 1), (1, 1), (2, 2), (1, 2), (2, 1)]), 3)
        self.assertEqual(extract_freq([(1, 2), (2, 1), (1, 1), (2, 2), (1, 2), (2, 1), (1, 2)]), 3)
        self.assertEqual(extract_freq([(1, 2), (2, 1), (1, 1), (2, 2), (1, 2), (2, 1), (1, 2), (1, 2)]), 3)

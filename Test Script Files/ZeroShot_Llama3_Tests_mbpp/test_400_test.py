import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):

    def test_extract_freq(self):
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3]]), 2)
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3], [1, 2, 3]]), 2)
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3], [1, 2, 3], [1, 2, 3]]), 2)
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]), 2)
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]), 2)
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]), 2)
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]), 2)
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]), 2)
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]), 2)
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]), 2)
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]), 2)
        self.assertEqual(extract_freq([[1, 2, 3], [3, 4, 5], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3
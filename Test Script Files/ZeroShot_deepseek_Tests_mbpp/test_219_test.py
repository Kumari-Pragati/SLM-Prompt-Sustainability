import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_extract_min_max(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 5))
        self.assertEqual(extract_min_max((5, 2, 3, 4, 1), 2), (1, 5))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 3), (1, 2, 5))
        self.assertEqual(extract_min_max((5, 4, 3, 2, 1), 3), (1, 2, 5))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 1), (1,))
        self.assertEqual(extract_min_max((5, 4, 3, 2, 1), 1), (1,))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), ())
        self.assertEqual(extract_min_max((5, 4, 3, 2, 1), 0), ())

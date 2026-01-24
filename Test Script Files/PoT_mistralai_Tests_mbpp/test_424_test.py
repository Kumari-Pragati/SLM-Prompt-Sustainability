import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):
    def test_typical(self):
        self.assertListEqual(extract_rear(([1], [2, 3], [4, 5, 6])), [6, 3, 5])
        self.assertListEqual(extract_rear(([1, 2], [3, 4], [5, 6, 7])), [7, 4, 6])

    def test_edge_and_boundary(self):
        self.assertListEqual(extract_rear(([])), [])
        self.assertListEqual(extract_rear(([1])), [1])
        self.assertListEqual(extract_rear(([1, 2], [3], [4, 5])), [5, 3])
        self.assertListEqual(extract_rear(([1, 2, 3], [4, 5], [6, 7, 8])), [8, 5, 7])

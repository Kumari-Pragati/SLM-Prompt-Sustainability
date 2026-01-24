import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):
    def test_symmetric_pair(self):
        self.assertCountEqual(extract_symmetric([(1, 2), (2, 1), (3, 4), (4, 3)]), [(1, 2)])

    def test_empty_list(self):
        self.assertCountEqual(extract_symmetric([]), [])

    def test_single_element(self):
        self.assertCountEqual(extract_symmetric([(1, 1)]), [])

    def test_non_symmetric_pair(self):
        self.assertCountEqual(extract_symmetric([(1, 2), (2, 3)]), [])

    def test_reverse_order(self):
        self.assertCountEqual(extract_symmetric([(2, 1), (1, 2)]), [(1, 2)])

    def test_negative_numbers(self):
        self.assertCountEqual(extract_symmetric([(-1, -2), (-2, -1)]), [(-1, -2)])

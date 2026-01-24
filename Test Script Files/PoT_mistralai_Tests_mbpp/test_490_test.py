import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):
    def test_typical(self):
        self.assertCountEqual(extract_symmetric([(1, 2), (2, 1), (3, 4), (4, 3)]), [(1, 2), (2, 1)])
        self.assertCountEqual(extract_symmetric([(1, 1), (2, 2), (3, 3)]), [])
        self.assertCountEqual(extract_symmetric([(1, 2), (2, 1), (1, 1)]), [])

    def test_edge_and_boundary(self):
        self.assertCountEqual(extract_symmetric([(1, 2), (2, 1), (1, 2), (2, 1)]), [(1, 2), (2, 1)])
        self.assertCountEqual(extract_symmetric([(1, 2), (2, 1), (0, 1), (1, 0)]), [])
        self.assertCountEqual(extract_symmetric([(1, 2), (2, 1), (1, 0)]), [])
        self.assertCountEqual(extract_symmetric([(1, 2), (2, 1), (1, 2), (2, 1), (0, 1)]), [(1, 2), (2, 1)])
        self.assertCountEqual(extract_symmetric([(1, 2), (2, 1), (1, 2), (2, 1), (0, 1), (1, 0)]), [])

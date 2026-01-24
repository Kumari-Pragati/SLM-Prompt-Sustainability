import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(check_K([1, 2, 3, 4], 3))
        self.assertFalse(check_K([1, 2, 3, 4], 5))

    def test_edge_cases(self):
        self.assertTrue(check_K([], 1))
        self.assertTrue(check_K([1], 1))
        self.assertFalse(check_K([1], 2))
        self.assertTrue(check_K([None], None))

    def test_complex(self):
        self.assertTrue(check_K([0, -1, 0, 0.0, None], 0))
        self.assertFalse(check_K([0, -1, 0, 0.0, None], 1))

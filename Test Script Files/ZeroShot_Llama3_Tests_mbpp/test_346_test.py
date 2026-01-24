import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):

    def test_zigzag_zero(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_zigzag_zero_k(self):
        self.assertEqual(zigzag(0, 1), 0)

    def test_zigzag_nonzero(self):
        self.assertEqual(zigzag(1, 1), 2)

    def test_zigzag_nonzero_k(self):
        self.assertEqual(zigzag(1, 2), 1)

    def test_zigzag_nonzero_n(self):
        self.assertEqual(zigzag(2, 1), 2)

    def test_zigzag_nonzero_nk(self):
        self.assertEqual(zigzag(2, 2), 2)

    def test_zigzag_nonzero_nk_zero(self):
        self.assertEqual(zigzag(2, 0), 0)

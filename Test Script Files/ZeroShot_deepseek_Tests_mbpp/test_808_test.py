import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):

    def test_positive_case(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5), 3))
        self.assertTrue(check_K((10, 20, 30, 40, 50), 20))
        self.assertTrue(check_K((100, 200, 300, 400, 500), 300))

    def test_negative_case(self):
        self.assertFalse(check_K((1, 2, 3, 4, 5), 6))
        self.assertFalse(check_K((10, 20, 30, 40, 50), 100))
        self.assertFalse(check_K((100, 200, 300, 400, 500), 600))

    def test_empty_tuple(self):
        self.assertFalse(check_K((), 1))
        self.assertFalse(check_K((), 0))

    def test_large_tuple(self):
        self.assertTrue(check_K((i for i in range(1, 1000001)), 500000))
        self.assertFalse(check_K((i for i in range(1, 1000001)), 1000002))

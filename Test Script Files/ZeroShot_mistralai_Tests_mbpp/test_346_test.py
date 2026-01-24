import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_k_zero(self):
        self.assertEqual(zigzag(n, 0), 0) for n in range(1, 10)

    def test_negative_n(self):
        self.assertEqual(zigzag(-1, 0), 0)
        self.assertEqual(zigzag(0, -1), 0)

    def test_k_greater_than_n(self):
        self.assertEqual(zigzag(1, 2), 0)
        self.assertEqual(zigzag(2, 3), 0)

    def test_k_equal_to_n(self):
        self.assertEqual(zigzag(1, 1), 1)
        self.assertEqual(zigzag(2, 2), 2)
        self.assertEqual(zigzag(3, 3), 4)

    def test_large_inputs(self):
        self.assertEqual(zigzag(10, 3), 55)
        self.assertEqual(zigzag(20, 10), 1024)

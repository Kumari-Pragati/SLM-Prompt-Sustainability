import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_min_Jumps_with_same_values(self):
        self.assertEqual(min_Jumps(5, 5, 10), 2)
        self.assertEqual(min_Jumps(10, 10, 0), 0)
        self.assertEqual(min_Jumps(15, 15, 15), 1)

    def test_min_Jumps_with_different_values(self):
        self.assertEqual(min_Jumps(10, 20, 15), 2)
        self.assertEqual(min_Jumps(20, 10, 15), 2)
        self.assertEqual(min_Jumps(10, 20, 25), 3)
        self.assertEqual(min_Jumps(20, 10, 25), 3)

    def test_min_Jumps_with_d_greater_than_or_equal_to_b(self):
        self.assertEqual(min_Jumps(10, 20, 30), 2)
        self.assertEqual(min_Jumps(20, 10, 30), 2)

    def test_min_Jumps_with_d_equal_to_zero(self):
        self.assertEqual(min_Jumps(10, 20, 0), 0)

    def test_min_Jumps_with_d_equal_to_a(self):
        self.assertEqual(min_Jumps(10, 20, 10), 1)

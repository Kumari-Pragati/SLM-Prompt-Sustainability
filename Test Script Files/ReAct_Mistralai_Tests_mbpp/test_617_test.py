import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(min_Jumps(5, 3, 2), 3)
        self.assertEqual(min_Jumps(3, 5, 2), 3)
        self.assertEqual(min_Jumps(2, 1, 1), 2)
        self.assertEqual(min_Jumps(1, 2, 1), 2)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(min_Jumps(0, 3, 2), 0)
        self.assertEqual(min_Jumps(-1, 3, 2), 2)
        self.assertEqual(min_Jumps(3, -1, 2), 2)
        self.assertEqual(min_Jumps(0, 0, 2), 0)
        self.assertEqual(min_Jumps(0, 0, 0), 0)

    def test_equal_numbers(self):
        self.assertEqual(min_Jumps(3, 3, 2), 1)
        self.assertEqual(min_Jumps(2, 2, 1), 2)

    def test_d_is_zero(self):
        self.assertEqual(min_Jumps(3, 2, 0), 0)

    def test_d_is_equal_to_a(self):
        self.assertEqual(min_Jumps(3, 2, 3), 1)

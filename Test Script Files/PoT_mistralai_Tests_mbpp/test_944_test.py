import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(num_position("hello123world"), 0)
        self.assertEqual(num_position("1234567890"), 0)
        self.assertEqual(num_position("a1b2c3"), 0)
        self.assertEqual(num_position("123a456"), 3)
        self.assertEqual(num_position("123 456 789"), 0)
        self.assertEqual(num_position("123\t456"), 0)
        self.assertEqual(num_position("123\n456"), 4)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(num_position(""), -1)
        self.assertEqual(num_position("0"), 0)
        self.assertEqual(num_position("1"), 0)
        self.assertEqual(num_position("12"), 0)
        self.assertEqual(num_position("12345678901234567890"), 0)
        self.assertEqual(num_position("123456789012345678901234567890"), 0)
        self.assertEqual(num_position("1234567890123456789012345678901"), 11)
        self.assertEqual(num_position("123456789012345678901234567890z"), -1)
        self.assertEqual(num_position("z12345678901234567890"), -1)
        self.assertEqual(num_position("12345678901234567890z"), -1)

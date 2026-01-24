import unittest

from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Sum(12), 10)

    def test_edge_case(self):
        self.assertEqual(find_Min_Sum(1), 1)
        self.assertEqual(find_Min_Sum(0), 0)

    def test_corner_case(self):
        self.assertEqual(find_Min_Sum(2), 2)
        self.assertEqual(find_Min_Sum(3), 3)
        self.assertEqual(find_Min_Sum(4), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Min_Sum("12")
        with self.assertRaises(ValueError):
            find_Min_Sum(-12)

import unittest

from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Nth_Digit(1, 2, 3), 1)

    def test_boundary_case(self):
        self.assertEqual(find_Nth_Digit(0, 1, 1), 0)

    def test_edge_case(self):
        self.assertEqual(find_Nth_Digit(10, 100, 2), 1)
        self.assertEqual(find_Nth_Digit(1, 1, 1), 1)
        self.assertEqual(find_Nth_Digit(1, 2, 0), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Nth_Digit("1", 2, 3)
        with self.assertRaises(TypeError):
            find_Nth_Digit(1, "2", 3)
        with self.assertRaises(TypeError):
            find_Nth_Digit(1, 2, "3")
        with self.assertRaises(ValueError):
            find_Nth_Digit(1, 2, -1)

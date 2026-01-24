import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(find_lucas(0), 2)
        self.assertEqual(find_lucas(1), 1)
        self.assertEqual(find_lucas(2), 3)
        self.assertEqual(find_lucas(3), 4)
        self.assertEqual(find_lucas(4), 7)

    def test_negative_input(self):
        self.assertRaises(ValueError, find_lucas, -1)

    def test_large_input(self):
        self.assertEqual(find_lucas(100), 2971215073)

    def test_zero_or_negative_recursion(self):
        self.assertRaises(RecursionError, find_lucas, 0)
        self.assertRaises(RecursionError, find_lucas, -1)

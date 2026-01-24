import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find(10, 2), 5)
        self.assertEqual(find(20, 4), 5)
        self.assertEqual(find(30, 5), 6)

    def test_edge_cases(self):
        self.assertEqual(find(1, 1), 1)
        self.assertEqual(find(0, 1), 0)
        self.assertEqual(find(1, 0), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)

    def test_negative_inputs(self):
        self.assertEqual(find(-10, 2), -5)
        self.assertEqual(find(10, -2), -5)

    def test_zero_inputs(self):
        self.assertEqual(find(0, 2), 0)
        self.assertEqual(find(10, 0), 0)

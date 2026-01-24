import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_str((1, 2), 3), [(1, 3), (2, 3)])

    def test_empty_tuple(self):
        self.assertEqual(add_str((), 3), [])

    def test_single_element_tuple(self):
        self.assertEqual(add_str((1,), 3), [(1, 3)])

    def test_large_tuple(self):
        self.assertEqual(add_str((1, 2, 3, 4, 5), 6), [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)])

    def test_negative_numbers(self):
        self.assertEqual(add_str((-1, -2), 3), [(-1, 3), (-2, 3)])

    def test_zero(self):
        self.assertEqual(add_str((0, 1), 0), [(0, 0), (1, 0)])

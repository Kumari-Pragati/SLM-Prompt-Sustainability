import unittest
from575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_count_no_basic(self):
        self.assertEqual(count_no(2, 3, 1, 5), 3)
        self.assertEqual(count_no(3, 1, 1, 3), 3)
        self.assertEqual(count_no(5, 1, 1, 5), 5)
        self.assertEqual(count_no(7, 1, 1, 7), 7)

    def test_count_no_edge_cases(self):
        self.assertEqual(count_no(2, 1, 1, 2), 2)
        self.assertEqual(count_no(2, 1, 2, 2), 2)
        self.assertEqual(count_no(2, 1, 3, 2), 3)
        self.assertEqual(count_no(2, 1, 4, 2), 4)

    def test_count_no_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            count_no(0, 1, 1, 1)

    def test_count_no_invalid_input(self):
        with self.assertRaises(ValueError):
            count_no(2, 1, 0, 5)
        with self.assertRaises(ValueError):
            count_no(2, 1, 5, 0)
        with self.assertRaises(ValueError):
            count_no(2, 0, 1, 5)
        with self.assertRaises(ValueError):
            count_no(2, 1, 5, 0)

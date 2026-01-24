import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):
    def test_count_no_with_valid_inputs(self):
        self.assertEqual(count_no(2, 5, 1, 10), 9)
        self.assertEqual(count_no(3, 3, 1, 10), 7)
        self.assertEqual(count_no(4, 4, 1, 10), 6)
        self.assertEqual(count_no(5, 5, 1, 10), 5)
        self.assertEqual(count_no(6, 5, 1, 10), 4)
        self.assertEqual(count_no(7, 5, 1, 10), 3)
        self.assertEqual(count_no(8, 5, 1, 10), 2)
        self.assertEqual(count_no(9, 5, 1, 10), 1)
        self.assertEqual(count_no(10, 5, 1, 10), 0)

    def test_count_no_with_invalid_inputs(self):
        self.assertRaises(ValueError, count_no, 0, 5, 1, 10)
        self.assertRaises(ValueError, count_no, 2, 0, 1, 10)
        self.assertRaises(ValueError, count_no, 2, 5, 0, 10)
        self.assertRaises(ValueError, count_no, 2, 5, 11, 10)
        self.assertRaises(ValueError, count_no, 2, 5, 1, -1)

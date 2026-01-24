import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_val([1, 2, 3]), 3)
        self.assertEqual(max_val([-1, 0, 1]), 1)
        self.assertEqual(max_val([5, 5, 5]), 5)

    def test_empty(self):
        self.assertIsNone(max_val([]))

    def test_non_int(self):
        with self.assertRaises(TypeError):
            max_val([1, 2, 'a', 4])

    def test_single_int(self):
        self.assertEqual(max_val([5]), 5)

    def test_multiple_int(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_negative(self):
        self.assertEqual(max_val([-1, -2, -3]), -1)

    def test_positive(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

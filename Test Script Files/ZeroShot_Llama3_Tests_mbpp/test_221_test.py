import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):

    def test_first_even(self):
        self.assertEqual(first_even([1, 2, 3, 4, 5]), 2)
        self.assertEqual(first_even([1, 3, 5, 7, 9]), -1)
        self.assertEqual(first_even([2, 4, 6, 8, 10]), 2)
        self.assertEqual(first_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 2)
        self.assertEqual(first_even([]), -1)
        self.assertEqual(first_even([1]), -1)
        self.assertEqual(first_even([2]), 2)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            first_even('hello')

    def test_non_integer_error(self):
        with self.assertRaises(TypeError):
            first_even([1, 2, 'a', 4, 5])

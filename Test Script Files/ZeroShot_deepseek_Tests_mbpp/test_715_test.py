import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):

    def test_str_to_tuple_with_valid_input(self):
        self.assertEqual(str_to_tuple('1, 2, 3'), (1, 2, 3))
        self.assertEqual(str_to_tuple('4, 5, 6'), (4, 5, 6))
        self.assertEqual(str_to_tuple('7, 8, 9'), (7, 8, 9))

    def test_str_to_tuple_with_invalid_input(self):
        self.assertRaises(ValueError, str_to_tuple, '1, 2, a')
        self.assertRaises(ValueError, str_to_tuple, '1, 2, 3, 4')
        self.assertRaises(ValueError, str_to_tuple, 'a, b, c')

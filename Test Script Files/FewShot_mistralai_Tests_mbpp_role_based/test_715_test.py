import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(str_to_tuple("1, 2, 3, 4"), (1, 2, 3, 4))
        self.assertEqual(str_to_tuple("5, 6, 7, 8"), (5, 6, 7, 8))

    def test_empty_input(self):
        self.assertIsInstance(str_to_tuple(""), tuple)
        self.assertIsInstance(str_to_tuple(" "), tuple)

    def test_single_input(self):
        self.assertIsInstance(str_to_tuple("1"), tuple)
        self.assertIsInstance(str_to_tuple("10"), tuple)

    def test_invalid_input(self):
        self.assertRaises(ValueError, str_to_tuple, "1, a, 3")
        self.assertRaises(ValueError, str_to_tuple, "1, 2, a, 4")
        self.assertRaises(ValueError, str_to_tuple, "1, 2, 3, a")

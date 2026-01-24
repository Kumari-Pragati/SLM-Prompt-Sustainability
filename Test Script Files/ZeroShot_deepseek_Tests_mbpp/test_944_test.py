import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):

    def test_num_position_with_numbers(self):
        self.assertEqual(num_position("123abc456"), 0)
        self.assertEqual(num_position("abc456"), 3)
        self.assertEqual(num_position("123abc"), 0)
        self.assertEqual(num_position("123456"), 0)

    def test_num_position_with_no_numbers(self):
        self.assertIsNone(num_position("abc"))
        self.assertIsNone(num_position(""))

    def test_num_position_with_special_characters(self):
        self.assertIsNone(num_position("!@#$%^&*"))

    def test_num_position_with_mixed_characters(self):
        self.assertEqual(num_position("abc123def"), 3)
        self.assertEqual(num_position("abc!@#123def"), 6)

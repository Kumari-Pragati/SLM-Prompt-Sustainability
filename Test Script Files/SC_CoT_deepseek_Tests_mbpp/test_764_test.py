import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(number_ctr("123abc"), 3)

    def test_empty_string(self):
        self.assertEqual(number_ctr(""), 0)

    def test_all_numbers(self):
        self.assertEqual(number_ctr("0123456789"), 10)

    def test_no_numbers(self):
        self.assertEqual(number_ctr("abcdefghijklmnopqrstuvwxyz"), 0)

    def test_special_characters(self):
        self.assertEqual(number_ctr("!@#$%^&*()"), 0)

    def test_mixed_case(self):
        self.assertEqual(number_ctr("123abc456def"), 6)

    def test_negative_case(self):
        with self.assertRaises(TypeError):
            number_ctr(12345)

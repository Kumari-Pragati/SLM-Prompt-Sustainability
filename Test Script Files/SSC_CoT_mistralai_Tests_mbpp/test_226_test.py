import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(odd_values_string("abcdefg"), "ac")
        self.assertEqual(odd_values_string("ABCDEFG"), "AB")
        self.assertEqual(odd_values_string("1234567"), "135")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(odd_values_string(""), "")
        self.assertEqual(odd_values_string("a"), "a")
        self.assertEqual(odd_values_string("aaa"), "a")
        self.assertEqual(odd_values_string("abcdefghijklmnopqrstuvwxyz"), "ab")
        self.assertEqual(odd_values_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "AB")
        self.assertEqual(odd_values_string("0123456789"), "1357")
        self.assertEqual(odd_values_string("!@#$%^&*()_+-={}[]|;:'\",.<>?/"), "!@#")

    def test_special_or_corner_cases(self):
        self.assertEqual(odd_values_string("aA1!"), "aA!")
        self.assertEqual(odd_values_string("12345678901234567890"), "1357901357")
        self.assertEqual(odd_values_string("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-={}[]|;:'\",.<>?/"), "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#")

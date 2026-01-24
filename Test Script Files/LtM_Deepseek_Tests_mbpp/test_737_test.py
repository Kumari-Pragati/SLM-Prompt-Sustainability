import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):

    def test_simple_valid_inputs(self):
        self.assertEqual(check_str('a123_'), "Valid")
        self.assertEqual(check_str('A456_'), "Valid")
        self.assertEqual(check_str('e789_'), "Valid")
        self.assertEqual(check_str('i012_'), "Valid")
        self.assertEqual(check_str('o345_'), "Valid")
        self.assertEqual(check_str('u678_'), "Valid")

    def test_edge_conditions(self):
        self.assertEqual(check_str(''), "Invalid")
        self.assertEqual(check_str('12345'), "Invalid")
        self.assertEqual(check_str('!@#$%'), "Invalid")
        self.assertEqual(check_str('A'), "Invalid")
        self.assertEqual(check_str('a'), "Invalid")
        self.assertEqual(check_str('I'), "Invalid")
        self.assertEqual(check_str('i'), "Invalid")

    def test_complex_cases(self):
        self.assertEqual(check_str('aeiouAEIOU'), "Valid")
        self.assertEqual(check_str('aeiouAEIOU12345'), "Valid")
        self.assertEqual(check_str('aeiouAEIOU!@#$%'), "Valid")
        self.assertEqual(check_str('aeiouAEIOU_'), "Valid")
        self.assertEqual(check_str('AEIOU'), "Invalid")
        self.assertEqual(check_str('aeiou'), "Invalid")
        self.assertEqual(check_str('12345'), "Invalid")
        self.assertEqual(check_str('!@#$%'), "Invalid")

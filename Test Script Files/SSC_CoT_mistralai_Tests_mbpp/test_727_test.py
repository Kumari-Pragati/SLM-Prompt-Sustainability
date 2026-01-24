import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_char("HelloWorld"), "HelloWorld")
        self.assertEqual(remove_char("123_abC_dEf"), "123abCdEf")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(remove_char(""), "")
        self.assertEqual(remove_char("_"), "")
        self.assertEqual(remove_char("__"), "")
        self.assertEqual(remove_char("___"), "")
        self.assertEqual(remove_char("____"), "")
        self.assertEqual(remove_char("_____"), "")
        self.assertEqual(remove_char("______"), "")
        self.assertEqual(remove_char("_______"), "")
        self.assertEqual(remove_char("________"), "")

    def test_special_and_corner_cases(self):
        self.assertEqual(remove_char("_HelloWorld_"), "HelloWorld")
        self.assertEqual(remove_char("HelloWorld_"), "HelloWorld")
        self.assertEqual(remove_char("_HelloWorld_"), "HelloWorld")
        self.assertEqual(remove_char("HelloWorld_"), "HelloWorld")
        self.assertEqual(remove_char("_HelloWorld_"), "HelloWorld")
        self.assertEqual(remove_char("HelloWorld_"), "HelloWorld")
        self.assertEqual(remove_char("_HelloWorld_"), "HelloWorld")
        self.assertEqual(remove_char("HelloWorld_"), "HelloWorld")
        self.assertEqual(remove_char("_HelloWorld_"), "HelloWorld")

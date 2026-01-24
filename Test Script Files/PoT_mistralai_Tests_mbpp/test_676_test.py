import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_extra_char("Hello_World_123"), "HelloWorld123")
        self.assertEqual(remove_extra_char("123_456_789"), "123456789")
        self.assertEqual(remove_extra_char("_Hello_World_"), "HelloWorld")

    def test_edge_case(self):
        self.assertEqual(remove_extra_char(""), "")
        self.assertEqual(remove_extra_char("_"), "")
        self.assertEqual(remove_extra_char("__"), "")
        self.assertEqual(remove_extra_char("___"), "")

    def test_boundary_case(self):
        self.assertEqual(remove_extra_char("_HelloWorld_"), "HelloWorld")
        self.assertEqual(remove_extra_char("Hello_World_"), "HelloWorld")
        self.assertEqual(remove_extra_char("Hello_World"), "HelloWorld")
        self.assertEqual(remove_extra_char("HelloWorld_"), "HelloWorld")

    def test_corner_case(self):
        self.assertEqual(remove_extra_char("_Hello_World_123_"), "HelloWorld123")
        self.assertEqual(remove_extra_char("_123_"), "123")
        self.assertEqual(remove_extra_char("_123"), "123")
        self.assertEqual(remove_extra_char("123_"), "123")

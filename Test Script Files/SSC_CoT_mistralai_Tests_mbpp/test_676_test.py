import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_extra_char("Hello_World"), "HelloWorld")
        self.assertEqual(remove_extra_char("123_456"), "123456")

    def test_edge_and_boundary_cases(self):
        self.assertEqual(remove_extra_char(""), "")
        self.assertEqual(remove_extra_char("_"), "")
        self.assertEqual(remove_extra_char("__"), "")
        self.assertEqual(remove_extra_char("___"), "")
        self.assertEqual(remove_extra_char("____"), "")
        self.assertEqual(remove_extra_char("_____"), "")
        self.assertEqual(remove_extra_char("Hello_World_"), "HelloWorld")
        self.assertEqual(remove_extra_char("Hello_World__"), "HelloWorld")
        self.assertEqual(remove_extra_char("_Hello_World_"), "HelloWorld")
        self.assertEqual(remove_extra_char("_Hello_World__"), "HelloWorld")

    def test_special_cases(self):
        self.assertEqual(remove_extra_char("Hello_World_123"), "HelloWorld123")
        self.assertEqual(remove_extra_char("123_Hello_World"), "123HelloWorld")
        self.assertEqual(remove_extra_char("_123Hello_World"), "123HelloWorld")
        self.assertEqual(remove_extra_char("_123Hello_World_"), "123HelloWorld")
        self.assertEqual(remove_extra_char("Hello_World_123_"), "HelloWorld123")
        self.assertEqual(remove_extra_char("Hello_World_123__"), "HelloWorld123")
        self.assertEqual(remove_extra_char("_Hello_World_123_"), "HelloWorld123")
        self.assertEqual(remove_extra_char("_Hello_World_123__"), "HelloWorld123")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, remove_extra_char, 123)
        self.assertRaises(TypeError, remove_extra_char, (1, 2, 3))
        self.assertRaises(TypeError, remove_extra_char, [1, 2, 3])
        self.assertRaises(TypeError, remove_extra_char, None)
        self.assertRaises(TypeError, remove_extra_char, True)
        self.assertRaises(TypeError, remove_extra_char, False)

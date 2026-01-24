import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_splchar("Hello_World"), "HelloWorld")
        self.assertEqual(remove_splchar("123_456"), "123456")
        self.assertEqual(remove_splchar("Hello_World_123"), "HelloWorld123")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(remove_splchar(""), "")
        self.assertEqual(remove_splchar(" "), "")
        self.assertEqual(remove_splchar("_"), "")
        self.assertEqual(remove_splchar("__"), "")
        self.assertEqual(remove_splchar("____"), "")
        self.assertEqual(remove_splchar("______"), "")
        self.assertEqual(remove_splchar("_______"), "")
        self.assertEqual(remove_splchar("________"), "")
        self.assertEqual(remove_splchar("_________"), "")
        self.assertEqual(remove_splchar("____________"), "")

    def test_special_cases(self):
        self.assertEqual(remove_splchar("_Hello_World_"), "HelloWorld")
        self.assertEqual(remove_splchar("Hello_World_"), "HelloWorld")
        self.assertEqual(remove_splchar("_Hello_World"), "HelloWorld")
        self.assertEqual(remove_splchar("Hello_World_"), "HelloWorld")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, remove_splchar, 123)
        self.assertRaises(TypeError, remove_splchar, (1, 2, 3))
        self.assertRaises(TypeError, remove_splchar, [1, 2, 3])
        self.assertRaises(TypeError, remove_splchar, None)

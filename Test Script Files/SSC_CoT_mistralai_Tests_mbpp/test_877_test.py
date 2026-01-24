import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sort_String("HelloWorld"), "alhElloOrdW")
        self.assertEqual(sort_String("Python"), "hPythonn")
        self.assertEqual(sort_String("123456789"), "123456789")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sort_String(""), "")
        self.assertEqual(sort_String("a"), "a")
        self.assertEqual(sort_String("abcdefghijklmnopqrstuvwxyz"), "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(sort_String("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(sort_String("01234567890"), "01234567890")
        self.assertEqual(sort_String("!@#$%^&*()_+-=[]{}|;':\"<>,.?/"), "!@#$%^&*()_+-=[]{}|;':\"<>,./")

    def test_special_or_corner_cases(self):
        self.assertEqual(sort_String("HelloWorld!"), "!alhElloOrdW")
        self.assertEqual(sort_String("123World456"), "123World456")
        self.assertEqual(sort_String("HelloWorld123"), "123alhElloOrdW")
        self.assertEqual(sort_String("123World!456"), "123World!456")
        self.assertEqual(sort_String("123World!456789"), "123World!456789")

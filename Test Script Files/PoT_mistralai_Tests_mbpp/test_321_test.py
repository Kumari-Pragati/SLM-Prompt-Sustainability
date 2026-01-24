import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(find_demlo("abc"), "12345abc")
        self.assertEqual(find_demlo(""), "")
        self.assertEqual(find_demlo("a"), "1a")
        self.assertEqual(find_demlo("abcdef"), "12345abcdef")

    def test_edge_cases(self):
        self.assertEqual(find_demlo("a"), "1a")
        self.assertEqual(find_demlo("a\t"), "1a\t")
        self.assertEqual(find_demlo("\n"), "")
        self.assertEqual(find_demlo(" "), "")
        self.assertEqual(find_demlo("1"), "1")
        self.assertEqual(find_demlo("12"), "121")
        self.assertEqual(find_demlo("12345"), "1234512345")
        self.assertEqual(find_demlo("123456"), "123456123456")
        self.assertEqual(find_demlo("1234567"), "12345671234567")

    def test_corner_cases(self):
        self.assertEqual(find_demlo("12345678901234567890"), "123456789012345678901234567890")
        self.assertEqual(find_demlo("1234567890123456789012345678901"), "1234567890123456789012345678901234567890")

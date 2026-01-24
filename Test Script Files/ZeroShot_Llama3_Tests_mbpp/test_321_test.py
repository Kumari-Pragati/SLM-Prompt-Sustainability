import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):

    def test_find_demlo(self):
        self.assertEqual(find_demlo("1"), "11")
        self.assertEqual(find_demlo("2"), "121")
        self.assertEqual(find_demlo("3"), "12321")
        self.assertEqual(find_demlo("4"), "1234321")
        self.assertEqual(find_demlo("5"), "123454321")
        self.assertEqual(find_demlo("6"), "12345654321")
        self.assertEqual(find_demlo("7"), "1234567654321")
        self.assertEqual(find_demlo("8"), "123456787654321")
        self.assertEqual(find_demlo("9"), "12345678987654321")
        self.assertEqual(find_demlo("10"), "123456789876543210")
        self.assertEqual(find_demlo(""), "")
        self.assertEqual(find_demlo("1"), "11")
        self.assertEqual(find_demlo("a"), "")
        self.assertEqual(find_demlo("123"), "123321")

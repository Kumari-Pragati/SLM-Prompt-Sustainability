import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_demlo("abc"), "1234abc")
        self.assertEqual(find_demlo("xyz"), "123xyz")
        self.assertEqual(find_demlo("123"), "123123")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_demlo(""), "")
        self.assertEqual(find_demlo("a"), "1a")
        self.assertEqual(find_demlo("aa"), "12aa")
        self.assertEqual(find_demlo("1"), "1")
        self.assertEqual(find_demlo("12"), "1212")
        self.assertEqual(find_demlo("1234"), "12341234")
        self.assertEqual(find_demlo("abcdefg"), "123456abcdefg")

    def test_special_or_corner_cases(self):
        self.assertEqual(find_demlo("0"), "0")
        self.assertEqual(find_demlo("10"), "1010")
        self.assertEqual(find_demlo("101"), "101101")
        self.assertEqual(find_demlo("10101"), "1010110101")

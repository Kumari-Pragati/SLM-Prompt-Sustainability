import unittest
from mbpp_950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(chinese_zodiac(2004), 'Monkey')

    def test_edge_case(self):
        self.assertEqual(chinese_zodiac(1999), 'Hare')

    def test_edge_case2(self):
        self.assertEqual(chinese_zodiac(2000), 'Dragon')

    def test_edge_case3(self):
        self.assertEqual(chinese_zodiac(2012), 'Dragon')

    def test_edge_case4(self):
        self.assertEqual(chinese_zodiac(2023), 'Rat')

    def test_edge_case5(self):
        self.assertEqual(chinese_zodiac(2024), 'Monkey')

    def test_edge_case6(self):
        self.assertEqual(chinese_zodiac(2025), 'Rooster')

    def test_edge_case7(self):
        self.assertEqual(chinese_zodiac(2030), 'Tiger')

    def test_edge_case8(self):
        self.assertEqual(chinese_zodiac(2031), 'Hare')

    def test_edge_case9(self):
        self.assertEqual(chinese_zodiac(2032), 'Dragon')

    def test_edge_case10(self):
        self.assertEqual(chinese_zodiac(2033), 'Snake')

    def test_edge_case11(self):
        self.assertEqual(chinese_zodiac(2034), 'Horse')

    def test_edge_case12(self):
        self.assertEqual(chinese_zodiac(2035),'sheep')

    def test_edge_case13(self):
        self.assertEqual(chinese_zodiac(2036), 'Monkey')

    def test_edge_case14(self):
        self.assertEqual(chinese_zodiac(2037), 'Rooster')

    def test_edge_case15(self):
        self.assertEqual(chinese_zodiac(2038), 'Dog')

    def test_edge_case16(self):
        self.assertEqual(chinese_zodiac(2039), 'Pig')

    def test_edge_case17(self):
        self.assertEqual(chinese_zodiac(2040), 'Rat')

    def test_edge_case18(self):
        self.assertEqual(chinese_zodiac(2041), 'Ox')

    def test_edge_case19(self):
        self.assertEqual(chinese_zodiac(2042), 'Tiger')

    def test_edge_case20(self):
        self.assertEqual(chinese_zodiac(2043), 'Hare')

    def test_edge_case21(self):
        self.assertEqual(chinese_zodiac(2044), 'Dragon')

    def test_edge_case22(self):
        self.assertEqual(chinese_zodiac(2045), 'Snake')

    def test_edge_case23(self):
        self.assertEqual(chinese_zodiac(2046), 'Horse')

    def test_edge_case24(self):
        self.assertEqual(chinese_zodiac(2047),'sheep')

    def test_edge_case25(self):
        self.assertEqual(chinese_zodiac(2048), 'Monkey')

    def test_edge_case26(self):
        self.assertEqual(chinese_zodiac(2049), 'Rooster')

    def test_edge_case27(self):
        self.assertEqual(chinese_zodiac(2050), 'Dog')

    def test_edge_case28(self):
        self.assertEqual(chinese_zodiac(2051), 'Pig')

    def test_edge_case29(self):
        self.assertEqual(chinese_zodiac(2052), 'Rat')

    def test_edge_case30(self):
        self.assertEqual(chinese_zodiac(2053), 'Ox')

    def test_edge_case31(self):
        self.assertEqual(chinese_zodiac(2054), 'Tiger')

    def test_edge_case32(self):
        self.assertEqual(chinese_zodiac(2055), 'Hare')

    def test_edge_case33(self):
        self.assertEqual(chinese_zodiac(2056), 'Dragon')

    def test_edge_case34(self):
        self.assertEqual(chinese_zodiac(2057), 'Snake')

    def test_edge_case35(self):
        self.assertEqual(chinese_zodiac(2058), 'Horse')

    def test_edge_case36(self):
        self.assertEqual(chinese_zodiac(2059),'sheep')

    def test_edge_case37(self):
        self.assertEqual(chinese_zodiac(2060), 'Monkey')

    def test_edge_case38(self):
        self.assertEqual(chinese_zodiac(2061), 'Rooster')

    def test_edge_case39(self):
        self.assertEqual(chinese_zodiac(2062), 'Dog')

    def test_edge_case40(self):
        self.assertEqual(chinese_zodiac(2063), 'Pig')

    def test_edge_case41(self):
        self.assertEqual(chinese_zodiac(2064), 'Rat')

    def test_edge_case42(self):
        self.assertEqual(chinese_zodiac(2065), 'Ox')

    def test_edge_case43(self):
        self.assertEqual(chinese_zodiac(2066), 'Tiger')

    def test_edge_case44(self
import unittest
from mbpp_950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):

    def test_valid_year(self):
        self.assertEqual(chinese_zodiac(2004), 'Dragon')
        self.assertEqual(chinese_zodiac(2005), 'Snake')
        self.assertEqual(chinese_zodiac(2006), 'Horse')
        self.assertEqual(chinese_zodiac(2007),'sheep')
        self.assertEqual(chinese_zodiac(2008), 'Monkey')
        self.assertEqual(chinese_zodiac(2009), 'Rooster')
        self.assertEqual(chinese_zodiac(2010), 'Dog')
        self.assertEqual(chinese_zodiac(2011), 'Pig')
        self.assertEqual(chinese_zodiac(2012), 'Rat')
        self.assertEqual(chinese_zodiac(2013), 'Ox')
        self.assertEqual(chinese_zodiac(2014), 'Tiger')
        self.assertEqual(chinese_zodiac(2015), 'Hare')

    def test_invalid_year(self):
        self.assertRaises(TypeError, chinese_zodiac, 'abc')
        self.assertRaises(TypeError, chinese_zodiac, 1000)
        self.assertRaises(TypeError, chinese_zodiac, 3000)

    def test_edge_cases(self):
        self.assertEqual(chinese_zodiac(1999), 'Hare')
        self.assertEqual(chinese_zodiac(2000), 'Dragon')
        self.assertEqual(chinese_zodiac(2001), 'Snake')
        self.assertEqual(chinese_zodiac(2020), 'Rat')

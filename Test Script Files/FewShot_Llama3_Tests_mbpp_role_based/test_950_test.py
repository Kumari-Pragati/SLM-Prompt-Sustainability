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

    def test_year_before_2000(self):
        self.assertEqual(chinese_zodiac(1999), 'Hare')

    def test_year_after_2000(self):
        self.assertEqual(chinese_zodiac(2020), 'Rat')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            chinese_zodiac('abc')

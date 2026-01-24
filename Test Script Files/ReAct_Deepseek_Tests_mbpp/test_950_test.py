import unittest
from mbpp_950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(chinese_zodiac(2000), 'Dragon')
        self.assertEqual(chinese_zodiac(2001), 'Snake')
        self.assertEqual(chinese_zodiac(2002), 'Horse')
        self.assertEqual(chinese_zodiac(2003), 'Sheep')
        self.assertEqual(chinese_zodiac(2004), 'Monkey')
        self.assertEqual(chinese_zodiac(2005), 'Rooster')
        self.assertEqual(chinese_zodiac(2006), 'Dog')
        self.assertEqual(chinese_zodiac(2007), 'Pig')
        self.assertEqual(chinese_zodiac(2008), 'Rat')
        self.assertEqual(chinese_zodiac(2009), 'Ox')
        self.assertEqual(chinese_zodiac(2010), 'Tiger')
        self.assertEqual(chinese_zodiac(2011), 'Hare')

    def test_boundary_cases(self):
        self.assertEqual(chinese_zodiac(1999), 'Dragon')
        self.assertEqual(chinese_zodiac(2000), 'Dragon')
        self.assertEqual(chinese_zodiac(2001), 'Snake')
        self.assertEqual(chinese_zodiac(2011), 'Hare')
        self.assertEqual(chinese_zodiac(2012), 'Dragon')

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            chinese_zodiac('2000')
        with self.assertRaises(ValueError):
            chinese_zodiac(-1)

import unittest
from mbpp_950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):
    def test_typical_cases(self):
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

    def test_edge_cases(self):
        self.assertEqual(chinese_zodiac(1999), 'Hare')
        self.assertEqual(chinese_zodiac(2000), 'Dragon')
        self.assertEqual(chinese_zodiac(2001), 'Snake')
        self.assertEqual(chinese_zodiac(2002), 'Horse')
        self.assertEqual(chinese_zodiac(2003),'sheep')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            chinese_zodiac('abc')
        with self.assertRaises(TypeError):
            chinese_zodiac(None)

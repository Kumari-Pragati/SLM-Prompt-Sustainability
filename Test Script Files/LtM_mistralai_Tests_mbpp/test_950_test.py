import unittest
from mbpp_950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):

    def test_simple_years(self):
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

    def test_edge_cases(self):
        self.assertEqual(chinese_zodiac(1999), 'Rat')
        self.assertEqual(chinese_zodiac(2011), 'Rabbit')
        self.assertEqual(chinese_zodiac(2020), 'Rat')
        self.assertEqual(chinese_zodiac(2021), 'Ox')

    def test_invalid_inputs(self):
        self.assertEqual(chinese_zodiac(-1), 'Hare')
        self.assertEqual(chinese_zodiac(float('inf')), 'Hare')
        self.assertEqual(chinese_zodiac(0), 'Hare')

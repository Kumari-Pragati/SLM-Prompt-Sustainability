import unittest
from mbpp_950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(chinese_zodiac(2004), 'Dragon')
        self.assertEqual(chinese_zodiac(2005), 'Snake')
        self.assertEqual(chinese_zodiac(2010), 'Tiger')
        self.assertEqual(chinese_zodiac(2011), 'Rabbit')
        self.assertEqual(chinese_zodiac(2019), 'Pig')

    def test_edge_cases(self):
        self.assertEqual(chinese_zodiac(1999), 'Hare')
        self.assertEqual(chinese_zodiac(2000), 'Dragon')
        self.assertEqual(chinese_zodiac(2001), 'Snake')
        self.assertEqual(chinese_zodiac(2002), 'Horse')
        self.assertEqual(chinese_zodiac(2003),'sheep')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            chinese_zodiac('a')
        with self.assertRaises(TypeError):
            chinese_zodiac(None)
        with self.assertRaises(TypeError):
            chinese_zodiac(123.45)

    def test_boundary_cases(self):
        self.assertEqual(chinese_zodiac(2004), 'Dragon')
        self.assertEqual(chinese_zodiac(2005), 'Snake')
        self.assertEqual(chinese_zodiac(2006), 'Horse')
        self.assertEqual(chinese_zodiac(2007),'sheep')
        self.assertEqual(chinese_zodiac(2008), 'Monkey')
        self.assertEqual(chinese_zodiac(2009), 'Rooster')

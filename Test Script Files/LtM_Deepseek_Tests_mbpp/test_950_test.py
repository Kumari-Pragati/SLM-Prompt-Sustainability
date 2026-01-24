import unittest
from mbpp_950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):

    # Test for typical years
    def test_typical_years(self):
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

    # Test for years near the start of the cycle
    def test_near_start_of_cycle(self):
        self.assertEqual(chinese_zodiac(1999), 'Hare')
        self.assertEqual(chinese_zodiac(1998), 'Tiger')
        self.assertEqual(chinese_zodiac(1997), 'Ox')
        self.assertEqual(chinese_zodiac(1996), 'Rat')
        self.assertEqual(chinese_zodiac(1995), 'Pig')
        self.assertEqual(chinese_zodiac(1994), 'Dog')
        self.assertEqual(chinese_zodiac(1993), 'Rooster')
        self.assertEqual(chinese_zodiac(1992), 'Monkey')
        self.assertEqual(chinese_zodiac(1991), 'Sheep')
        self.assertEqual(chinese_zodiac(1990), 'Horse')
        self.assertEqual(chinese_zodiac(1989), 'Snake')
        self.assertEqual(chinese_zodiac(1988), 'Dragon')

    # Test for years near the end of the cycle
    def test_near_end_of_cycle(self):
        self.assertEqual(chinese_zodiac(2021), 'Hare')
        self.assertEqual(chinese_zodiac(2022), 'Tiger')
        self.assertEqual(chinese_zodiac(2023), 'Ox')
        self.assertEqual(chinese_zodiac(2024), 'Rat')
        self.assertEqual(chinese_zodiac(2025), 'Pig')
        self.assertEqual(chinese_zodiac(2026), 'Dog')
        self.assertEqual(chinese_zodiac(2027), 'Rooster')
        self.assertEqual(chinese_zodiac(2028), 'Monkey')
        self.assertEqual(chinese_zodiac(2029), 'Sheep')
        self.assertEqual(chinese_zodiac(2030), 'Horse')
        self.assertEqual(chinese_zodiac(2031), 'Snake')
        self.assertEqual(chinese_zodiac(2032), 'Dragon')

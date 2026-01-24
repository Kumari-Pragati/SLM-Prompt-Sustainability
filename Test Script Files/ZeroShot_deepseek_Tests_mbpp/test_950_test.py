import unittest
from mbpp_950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):

    def test_dragon(self):
        self.assertEqual(chinese_zodiac(2000), 'Dragon')
        self.assertEqual(chinese_zodiac(2012), 'Dragon')

    def test_snake(self):
        self.assertEqual(chinese_zodiac(2001), 'Snake')
        self.assertEqual(chinese_zodiac(2013), 'Snake')

    def test_horse(self):
        self.assertEqual(chinese_zodiac(2002), 'Horse')
        self.assertEqual(chinese_zodiac(2014), 'Horse')

    def test_sheep(self):
        self.assertEqual(chinese_zodiac(2003), 'sheep')
        self.assertEqual(chinese_zodiac(2015), 'sheep')

    def test_monkey(self):
        self.assertEqual(chinese_zodiac(2004), 'Monkey')
        self.assertEqual(chinese_zodiac(2016), 'Monkey')

    def test_rooster(self):
        self.assertEqual(chinese_zodiac(2005), 'Rooster')
        self.assertEqual(chinese_zodiac(2017), 'Rooster')

    def test_dog(self):
        self.assertEqual(chinese_zodiac(2006), 'Dog')
        self.assertEqual(chinese_zodiac(2018), 'Dog')

    def test_pig(self):
        self.assertEqual(chinese_zodiac(2007), 'Pig')
        self.assertEqual(chinese_zodiac(2019), 'Pig')

    def test_rat(self):
        self.assertEqual(chinese_zodiac(2008), 'Rat')
        self.assertEqual(chinese_zodiac(2020), 'Rat')

    def test_ox(self):
        self.assertEqual(chinese_zodiac(2009), 'Ox')
        self.assertEqual(chinese_zodiac(2021), 'Ox')

    def test_tiger(self):
        self.assertEqual(chinese_zodiac(2010), 'Tiger')
        self.assertEqual(chinese_zodiac(2022), 'Tiger')

    def test_hare(self):
        self.assertEqual(chinese_zodiac(2011), 'Hare')
        self.assertEqual(chinese_zodiac(2023), 'Hare')

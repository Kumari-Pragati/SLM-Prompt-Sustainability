import unittest
from mbpp_950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):

    def test_dragon_sign(self):
        self.assertEqual(chinese_zodiac(2012), 'Dragon')
        self.assertEqual(chinese_zodiac(2024), 'Dragon')

    def test_snake_sign(self):
        self.assertEqual(chinese_zodiac(2008), 'Snake')
        self.assertEqual(chinese_zodiac(2020), 'Snake')

    def test_horse_sign(self):
        self.assertEqual(chinese_zodiac(2010), 'Horse')
        self.assertEqual(chinese_zodiac(2022), 'Horse')

    def test_sheep_sign(self):
        self.assertEqual(chinese_zodiac(2013), 'Sheep')
        self.assertEqual(chinese_zodiac(2025), 'Sheep')

    def test_monkey_sign(self):
        self.assertEqual(chinese_zodiac(2009), 'Monkey')
        self.assertEqual(chinese_zodiac(2021), 'Monkey')

    def test_rooster_sign(self):
        self.assertEqual(chinese_zodiac(2011), 'Rooster')
        self.assertEqual(chinese_zodiac(2023), 'Rooster')

    def test_dog_sign(self):
        self.assertEqual(chinese_zodiac(2014), 'Dog')
        self.assertEqual(chinese_zodiac(2026), 'Dog')

    def test_pig_sign(self):
        self.assertEqual(chinese_zodiac(2015), 'Pig')
        self.assertEqual(chinese_zodiac(2027), 'Pig')

    def test_rat_sign(self):
        self.assertEqual(chinese_zodiac(2005), 'Rat')
        self.assertEqual(chinese_zodiac(2017), 'Rat')

    def test_ox_sign(self):
        self.assertEqual(chinese_zodiac(2006), 'Ox')
        self.assertEqual(chinese_zodiac(2018), 'Ox')

    def test_tiger_sign(self):
        self.assertEqual(chinese_zodiac(2007), 'Tiger')
        self.assertEqual(chinese_zodiac(2019), 'Tiger')

    def test_hare_sign(self):
        self.assertEqual(chinese_zodiac(2000), 'Hare')
        self.assertEqual(chinese_zodiac(2002), 'Hare')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            chinese_zodiac('2000')
        with self.assertRaises(TypeError):
            chinese_zodiac(2000.0)
        with self.assertRaises(TypeError):
            chinese_zodiac(None)

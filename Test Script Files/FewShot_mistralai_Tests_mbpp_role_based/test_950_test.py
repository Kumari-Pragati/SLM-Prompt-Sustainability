import unittest
from mbpp_950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):
    def test_valid_years(self):
        self.assertEqual(chinese_zodiac(2000), 'Dragon')
        self.assertEqual(chinese_zodiac(2001), 'Snake')
        self.assertEqual(chinese_zodiac(2018), 'Dog')
        self.assertEqual(chinese_zodiac(2019), 'Pig')
        self.assertEqual(chinese_zodiac(2020), 'Rat')
        self.assertEqual(chinese_zodiac(2021), 'Ox')
        self.assertEqual(chinese_zodiac(2022), 'Tiger')

    def test_edge_cases(self):
        self.assertEqual(chinese_zodiac(1999), 'Rat')
        self.assertEqual(chinese_zodiac(20011), 'Dragon')
        self.assertEqual(chinese_zodiac(1900), 'Rat')
        self.assertEqual(chinese_zodiac(3000), 'Hare')

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, chinese_zodiac, 'string')
        self.assertRaises(TypeError, chinese_zodiac, -1)
        self.assertRaises(TypeError, chinese_zodiac, float('nan'))

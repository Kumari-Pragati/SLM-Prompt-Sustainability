import unittest
from mbpp_950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(chinese_zodiac(2012), 'Dragon')
        self.assertEqual(chinese_zodiac(2024), 'Monkey')
        self.assertEqual(chinese_zodiac(2008), 'Rooster')

    def test_boundary_conditions(self):
        self.assertEqual(chinese_zodiac(2000), 'Dragon')
        self.assertEqual(chinese_zodiac(2099), 'Hare')

    def test_edge_conditions(self):
        self.assertEqual(chinese_zodiac(1999), 'Hare')
        self.assertEqual(chinese_zodiac(2100), 'Dragon')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            chinese_zodiac('year')

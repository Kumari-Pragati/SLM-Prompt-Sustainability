import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):

    def test_wind_chill_positive_t_and_v(self):
        self.assertEqual(wind_chill(10, 10), 10)
        self.assertEqual(wind_chill(20, 20), 20)
        self.assertEqual(wind_chill(30, 30), 30)

    def test_wind_chill_negative_t_and_v(self):
        self.assertEqual(wind_chill(-10, -10), -10)
        self.assertEqual(wind_chill(-20, -20), -20)
        self.assertEqual(wind_chill(-30, -30), -30)

    def test_wind_chill_positive_t_and_negative_v(self):
        self.assertEqual(wind_chill(10, -10), -10)
        self.assertEqual(wind_chill(20, -20), -20)
        self.assertEqual(wind_chill(30, -30), -30)

    def test_wind_chill_negative_t_and_positive_v(self):
        self.assertEqual(wind_chill(-10, 10), -10)
        self.assertEqual(wind_chill(-20, 20), -20)
        self.assertEqual(wind_chill(-30, 30), -30)

import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(wind_chill(10, 5), 25)
        self.assertEqual(wind_chill(20, 10), 50)
        self.assertEqual(wind_chill(30, 0), 30)

    def test_edge_inputs(self):
        self.assertEqual(wind_chill(0, 100), 100)
        self.assertEqual(wind_chill(100, -100), 0)
        self.assertEqual(wind_chill(0, 0), 0)

    def test_complex_inputs(self):
        self.assertEqual(wind_chill(15, -20), -30)
        self.assertEqual(wind_chill(40, 40), 0)
        self.assertEqual(wind_chill(50, 30), 10)

import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):

    def test_positive_radius(self):
        self.assertEqual(rombus_perimeter(5), 20)

    def test_zero_radius(self):
        with self.assertRaises(TypeError):
            rombus_perimeter(0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            rombus_perimeter(-5)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            rombus_perimeter('five')

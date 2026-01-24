import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(rombus_perimeter(5), 20)

    def test_zero(self):
        self.assertEqual(rombus_perimeter(0), 0)

    def test_negative_integer(self):
        self.assertEqual(rombus_perimeter(-3), -12)

    def test_positive_float(self):
        self.assertAlmostEqual(rombus_perimeter(2.5), 10.0)

    def test_negative_float(self):
        self.assertAlmostEqual(rombus_perimeter(-1.5), -6.0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            rombus_perimeter("a")

    def test_non_numeric_input_2(self):
        with self.assertRaises(TypeError):
            rombus_perimeter(None)

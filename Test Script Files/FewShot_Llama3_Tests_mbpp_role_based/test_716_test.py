import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):
    def test_positive_input(self):
        self.assertEqual(rombus_perimeter(5), 20)

    def test_zero_input(self):
        self.assertEqual(rombus_perimeter(0), 0)

    def test_negative_input(self):
        self.assertEqual(rombus_perimeter(-5), 20)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            rombus_perimeter('a')

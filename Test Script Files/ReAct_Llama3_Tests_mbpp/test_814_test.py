import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(rombus_area(5, 3), 7.5)

    def test_negative_values(self):
        self.assertRaises(ZeroDivisionError, rombus_area, -5, 3)

    def test_zero_values(self):
        self.assertRaises(ZeroDivisionError, rombus_area, 0, 3)

    def test_zero_p(self):
        self.assertRaises(ZeroDivisionError, rombus_area, 0, 0)

    def test_zero_q(self):
        self.assertRaises(ZeroDivisionError, rombus_area, 3, 0)

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            rombus_area('five', 3)

    def test_non_numeric_p(self):
        with self.assertRaises(TypeError):
            rombus_area('five', 3)

    def test_non_numeric_q(self):
        with self.assertRaises(TypeError):
            rombus_area(5, 'three')

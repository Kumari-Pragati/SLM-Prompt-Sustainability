import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rombus_area(4, 5), 10)

    def test_zero_p(self):
        with self.assertRaises(ZeroDivisionError):
            rombus_area(0, 5)

    def test_zero_q(self):
        with self.assertRaises(ZeroDivisionError):
            rombus_area(5, 0)

    def test_negative_p(self):
        self.assertEqual(rombus_area(-4, 5), 10)

    def test_negative_q(self):
        self.assertEqual(rombus_area(4, -5), 10)

    def test_positive_p_and_q(self):
        self.assertEqual(rombus_area(2, 3), 3)

    def test_zero_p_and_q(self):
        with self.assertRaises(ZeroDivisionError):
            rombus_area(0, 0)

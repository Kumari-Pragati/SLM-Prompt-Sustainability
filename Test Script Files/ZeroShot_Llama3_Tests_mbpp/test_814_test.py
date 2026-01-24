import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):

    def test_positive_p_and_q(self):
        self.assertEqual(rombus_area(5, 3), 12.5)

    def test_negative_p_and_q(self):
        self.assertEqual(rombus_area(-5, -3), 12.5)

    def test_zero_p_and_q(self):
        self.assertEqual(rombus_area(0, 0), 0)

    def test_zero_p_and_non_zero_q(self):
        self.assertEqual(rombus_area(0, 3), 0)

    def test_non_zero_p_and_zero_q(self):
        self.assertEqual(rombus_area(5, 0), 0)

    def test_non_integer_p_and_q(self):
        self.assertEqual(rombus_area(5.5, 3.5), 12.375)

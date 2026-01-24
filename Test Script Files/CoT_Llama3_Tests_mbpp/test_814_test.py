import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(rombus_area(5, 3), 7.5)

    def test_negative_numbers(self):
        self.assertEqual(rombus_area(-5, -3), 7.5)

    def test_zero_area(self):
        self.assertEqual(rombus_area(0, 0), 0)

    def test_zero_p(self):
        self.assertEqual(rombus_area(0, 3), 0)

    def test_zero_q(self):
        self.assertEqual(rombus_area(5, 0), 0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            rombus_area('a', 3)

    def test_non_numeric_input2(self):
        with self.assertRaises(TypeError):
            rombus_area(5, 'b')

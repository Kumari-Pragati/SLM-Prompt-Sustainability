import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(rombus_area(5, 3), 7.5)

    def test_zero_value(self):
        self.assertEqual(rombus_area(0, 3), 0)

    def test_negative_values(self):
        self.assertEqual(rombus_area(-5, 3), 7.5)

    def test_zero_area(self):
        self.assertEqual(rombus_area(0, 0), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            rombus_area('a', 3)

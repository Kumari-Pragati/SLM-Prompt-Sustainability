import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(rombus_area(1, 2), 1)
        self.assertEqual(rombus_area(3, 4), 6)
        self.assertEqual(rombus_area(5, 6), 15)

    def test_zero_input(self):
        self.assertEqual(rombus_area(0, 1), 0)
        self.assertEqual(rombus_area(1, 0), 0)

    def test_negative_inputs(self):
        self.assertEqual(rombus_area(-1, 2), 1)
        self.assertEqual(rombus_area(1, -2), 1)
        self.assertEqual(rombus_area(-1, -2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rombus_area('a', 2)
        with self.assertRaises(TypeError):
            rombus_area(1, 'b')

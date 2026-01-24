import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(rombus_area(5, 3), 7.5)

    def test_edge_cases(self):
        self.assertEqual(rombus_area(0, 0), 0)
        self.assertEqual(rombus_area(0, 1), 0.5)
        self.assertEqual(rombus_area(1, 0), 0)

    def test_negative_inputs(self):
        self.assertEqual(rombus_area(-5, 3), 7.5)
        self.assertEqual(rombus_area(5, -3), 7.5)

    def test_zero_inputs(self):
        self.assertEqual(rombus_area(0, 0), 0)
        self.assertEqual(rombus_area(0, 1), 0.5)
        self.assertEqual(rombus_area(1, 0), 0)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            rombus_area('a', 3)
        with self.assertRaises(TypeError):
            rombus_area(5, 'b')

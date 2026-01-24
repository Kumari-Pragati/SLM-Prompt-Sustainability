import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(area_trapezium(2, 3, 4), 6)
        self.assertEqual(area_trapezium(5, 6, 7), 15.5)
        self.assertEqual(area_trapezium(1, 1, 1), 0.5)

    def test_edge_cases(self):
        self.assertEqual(area_trapezium(0, 0, 4), 0)
        self.assertEqual(area_trapezium(0, 0, 0), 0)
        self.assertEqual(area_trapezium(10, 10, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            area_trapezium('a', 3, 4)
        with self.assertRaises(TypeError):
            area_trapezium(2, 'b', 4)
        with self.assertRaises(TypeError):
            area_trapezium(2, 3, 'c')

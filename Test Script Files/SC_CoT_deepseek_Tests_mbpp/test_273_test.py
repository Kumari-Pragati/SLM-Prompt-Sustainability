import unittest

from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(substract_elements((10, 20, 30), (5, 10, 15)), (5, 10, 15))

    def test_edge_cases(self):
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), (0, 0, 0))
        self.assertEqual(substract_elements((100, 200, 300), (100, 200, 300)), (0, 0, 0))

    def test_corner_cases(self):
        self.assertEqual(substract_elements((-10, -20, -30), (10, 20, 30)), (-20, -40, -60))
        self.assertEqual(substract_elements((10, 20, 30), (-10, -20, -30)), (20, 40, 60))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            substract_elements((10, 20, 30), 5)
        with self.assertRaises(TypeError):
            substract_elements(10, (5, 10, 15))
        with self.assertRaises(TypeError):
            substract_elements((10, 20, 30), (5, '10', 15))

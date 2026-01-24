import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-4, -3, -3)))
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), ((0, 0, 0)))

    def test_edge_case_zero_length(self):
        self.assertEqual(substract_elements((1, 2, 3), ()), ((1, 2, 3)))
        self.assertEqual(substract_elements((), (1, 2, 3)), ((-1, -2, -3)))

    def test_edge_case_negative_numbers(self):
        self.assertEqual(substract_elements((-1, -2, -3), (4, 5, 6)), ((5, 7, 9)))
        self.assertEqual(substract_elements((1, 2, 3), (-4, -5, -6)), ((-5, -7, -9)))

    def test_edge_case_mixed_types(self):
        self.assertRaises(TypeError, substract_elements, (1, 2, 3), (4, '5', 6))
        self.assertRaises(TypeError, substract_elements, (1, 2, 3), (4, 5, '6'))

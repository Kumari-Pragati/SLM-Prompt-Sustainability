import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), (-3, -3, -3))

    def test_edge_cases(self):
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), (0, 0, 0))
        self.assertEqual(substract_elements((1, 2, 3), (3, 2, 1)), (-2, 0, 2))

    def test_negative_numbers(self):
        self.assertEqual(substract_elements((-1, -2, -3), (4, 5, 6)), (-5, -7, -9))

    def test_single_element_tuples(self):
        self.assertEqual(substract_elements((1,), (2,)), (-1,))
        self.assertEqual(substract_elements((1, 2), (1,)), (-1, 1))

    def test_empty_tuples(self):
        self.assertEqual(substract_elements((), ()), ())
        self.assertEqual(substract_elements((1, 2), ()), (1, 2))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            substract_elements('test', (1, 2, 3))

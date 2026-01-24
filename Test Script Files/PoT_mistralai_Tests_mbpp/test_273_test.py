import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(substract_elements((1, 2, 3), (2, 3, 4)), (-1, 1, -1))

    def test_edge_case_zero(self):
        self.assertEqual(substract_elements((0, 0, 0), (1, 2, 3)), (-1, -2, -3))

    def test_edge_case_negative(self):
        self.assertEqual(substract_elements((-1, -2, -3), (1, 2, 3)), (2, 4, 6))

    def test_edge_case_empty(self):
        self.assertEqual(substract_elements((), (1, 2, 3)), ())

    def test_edge_case_single_element(self):
        self.assertEqual(substract_elements((1,), (2, 3)), (-1,))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            substract_elements('1', '2')

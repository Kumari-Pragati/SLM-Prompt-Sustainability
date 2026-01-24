import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_substract_elements_normal(self):
        self.assertEqual(substract_elements((1, 2, 3), (2, 3, 4)), (-1, 1, -1))
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), (0, 0, 0))

    def test_substract_elements_edge_cases(self):
        self.assertEqual(substract_elements((1, 2, 3), (0, 0, 0)), (1, 2, 3))
        self.assertEqual(substract_elements((0, 0, 0), (1, 2, 3)), ((-1, -2, -3),))
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-3, -3, -3),))
        self.assertEqual(substract_elements((4, 5, 6), (1, 2, 3)), ((3, 3, 3),))

    def test_substract_elements_negative_numbers(self):
        self.assertEqual(substract_elements((-1, -2, -3), (2, 3, 4)), ((-3, -5, -7),))
        self.assertEqual(substract_elements((2, 3, 4), (-1, -2, -3)), ((3, 5, 7),))

    def test_substract_elements_mixed_types(self):
        with self.assertRaises(TypeError):
            substract_elements((1, 2, 3), (2, 3, "a"))
        with self.assertRaises(TypeError):
            substract_elements((1, 2, "a"), (2, 3, 4))

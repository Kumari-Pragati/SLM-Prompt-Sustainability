import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), (-3, -3, -3))

    def test_edge_case(self):
        self.assertEqual(substract_elements((1, 2, 3), (3, 2, 1)), (2, 4, 2))

    def test_edge_case2(self):
        self.assertEqual(substract_elements((1, 2, 3), (1, 2, 3)), (0, 0, 0))

    def test_edge_case3(self):
        self.assertEqual(substract_elements((), (1, 2, 3)), ())

    def test_edge_case4(self):
        self.assertEqual(substract_elements((1, 2, 3), ()), (1, 2, 3))

    def test_edge_case5(self):
        self.assertEqual(substract_elements((1, 2), (3, 4)), (-2, -2))

    def test_edge_case6(self):
        self.assertEqual(substract_elements((1, 2, 3, 4), (3, 2, 1, 0)), (2, 4, 2, 4))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            substract_elements('a', (1, 2, 3))

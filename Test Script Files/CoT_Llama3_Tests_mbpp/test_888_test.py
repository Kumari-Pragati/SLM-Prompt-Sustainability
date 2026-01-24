import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-3, -3, -3),))

    def test_edge_case1(self):
        self.assertEqual(substract_elements((1, 2), (3, 4)), ((-2, -2),))

    def test_edge_case2(self):
        self.assertEqual(substract_elements((1, 2, 3), ()), ((1, 2, 3),))

    def test_edge_case3(self):
        self.assertEqual(substract_elements((), (1, 2, 3)), ((1, 2, 3),))

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            substract_elements('test', (1, 2, 3))

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            substract_elements((1, 2, 3), 'test')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            substract_elements('test', 'test')

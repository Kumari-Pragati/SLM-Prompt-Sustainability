import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):
    def test_empty_tuples(self):
        self.assertEqual(index_multiplication((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(index_multiplication((1), (2)), (2,))
        self.assertEqual(index_multiplication((2), (1)), (2,))

    def test_equal_length_tuples(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((4*1, 5*2, 6*3),))
        self.assertEqual(index_multiplication((4, 5, 6), (1, 2, 3)), ((4*1, 5*2, 6*3),))

    def test_inequal_length_tuples(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5)), ((4*1, 5*2), 3*None))
        self.assertEqual(index_multiplication((4, 5), (1, 2, 3)), ((4*1, 5*2), 3*None))

    def test_negative_numbers(self):
        self.assertEqual(index_multiplication((-1, 2), (3, -4)), ((-3*1, 2*3), -4*2))
        self.assertEqual(index_multiplication((3, -4), (-1, 2)), ((3*1, -4*2), -1*2))

    def test_floats(self):
        self.assertListEqual(list(index_multiplication((1.5, 2.5), (3, 4))), [4.5*1.5, 5*2.5])
        self.assertListEqual(list(index_multiplication((3, 4), (1.5, 2.5))), [4.5*1.5, 5*2.5])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, index_multiplication, (1, 2), '3')
        self.assertRaises(TypeError, index_multiplication, '1', (2, 3))

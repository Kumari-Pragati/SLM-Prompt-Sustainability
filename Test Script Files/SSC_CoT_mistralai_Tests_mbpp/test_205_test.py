import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(inversion_elements((1, 2, 3, 4)), (0, 1, 2, 3))
        self.assertEqual(inversion_elements((0, -1, -2, -3)), (1, 0, -1, -2))
        self.assertEqual(inversion_elements((True, False, False, True)), (False, True, True, False))

    def test_edge_cases(self):
        self.assertEqual(inversion_elements(()), (1,))
        self.assertEqual(inversion_elements((0,)), (1,))
        self.assertEqual(inversion_elements((0, 0)), (1,))
        self.assertEqual(inversion_elements((1, 0, 0)), (0, 1, 1))
        self.assertEqual(inversion_elements((1, 1, 1)), (0, 0, 0))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, inversion_elements, 'abc')
        self.assertRaises(TypeError, inversion_elements, [1, 2, 3, 'a'])

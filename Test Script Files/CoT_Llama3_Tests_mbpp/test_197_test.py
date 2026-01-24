import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_exponentio((1, 2, 3), (4, 5, 6)), (1**4, 2**5, 3**6))

    def test_edge_cases(self):
        self.assertEqual(find_exponentio((0, 0), (0, 0)), (1, 1))
        self.assertEqual(find_exponentio((1, 2), (0, 0)), (1, 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_exponentio('test', (1, 2, 3))
        with self.assertRaises(TypeError):
            find_exponentio((1, 2, 3), 'test')

    def test_empty_inputs(self):
        self.assertEqual(find_exponentio((), ()), ())

    def test_single_element_inputs(self):
        self.assertEqual(find_exponentio((1,), (2,)), (1**2,))
        self.assertEqual(find_exponentio((1, 2), (3,)), (1**3, 2**3))

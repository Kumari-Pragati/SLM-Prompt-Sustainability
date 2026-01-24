import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (3, 4, 5)), ((1, 2), (4, 5)))

    def test_edge_condition(self):
        self.assertEqual(find_dissimilar((), ()), ())

    def test_boundary_condition(self):
        self.assertEqual(find_dissimilar((1,), (1,)), ())

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_dissimilar(123, (3, 4, 5))
        with self.assertRaises(TypeError):
            find_dissimilar((1, 2, 3), 'abc')

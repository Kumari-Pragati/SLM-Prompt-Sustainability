import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (3, 4, 5)), ((1, 2), (4, 5)))
        self.assertEqual(find_dissimilar((1, 1, 2), (1, 2, 3)), ((3),))
        self.assertEqual(find_dissimilar((), (1, 2, 3)), ((1, 2, 3),))
        self.assertEqual(find_dissimilar((1, 2, 3),()), ((1, 2, 3),))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_dissimilar((1,), (1,)), ())
        self.assertEqual(find_dissimilar((1,), (1, 1)), ())
        self.assertEqual(find_dissimilar((1, 1, 1), (1, 1, 1)), ())
        self.assertEqual(find_dissimilar((1, 1, 1), (1, 2, 1)), ((2,),))
        self.assertEqual(find_dissimilar((1, 1, 1), (1, 1, 2)), ((2,),))
        self.assertEqual(find_dissimilar((1, 1, 1), (1, 1, 1, 1)), ())

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_dissimilar, 1, 2)
        self.assertRaises(TypeError, find_dissimilar, (1, 'a'), (1, 2))

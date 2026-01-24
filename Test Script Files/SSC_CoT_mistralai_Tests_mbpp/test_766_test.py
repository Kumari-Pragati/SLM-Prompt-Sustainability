import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):

    def test_pair_wise_normal(self):
        self.assertEqual(pair_wise([1, 2, 3, 4]), [(1, 2), (2, 3), (3, 4)])
        self.assertEqual(pair_wise(["a", "b", "c", "d"]), [("a", "b"), ("b", "c"), ("c", "d")])

    def test_pair_wise_edge_cases(self):
        self.assertEqual(pair_wise([]), [])
        self.assertEqual(pair_wise([1]), [(1, None)])
        self.assertEqual(pair_wise([1, 2]), [(1, 2)])
        self.assertEqual(pair_wise([1, 2, 3]), [(1, 2), (2, 3)])
        self.assertEqual(pair_wise([1, 2, 3, 4, 5]), [(1, 2), (2, 3), (3, 4), (4, 5)])

    def test_pair_wise_invalid_inputs(self):
        with self.assertRaises(TypeError):
            pair_wise(123)
        with self.assertRaises(TypeError):
            pair_wise((1, 2, 3))

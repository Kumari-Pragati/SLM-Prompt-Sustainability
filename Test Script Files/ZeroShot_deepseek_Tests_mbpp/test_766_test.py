import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):

    def test_pair_wise(self):
        self.assertEqual(pair_wise([1, 2, 3, 4]), [(1, 2), (2, 3), (3, 4)])
        self.assertEqual(pair_wise(['a', 'b', 'c', 'd']), [('a', 'b'), ('b', 'c'), ('c', 'd')])
        self.assertEqual(pair_wise([True, False, True]), [(True, False), (False, True)])
        self.assertEqual(pair_wise([]), [])
        self.assertEqual(pair_wise([1]), [])

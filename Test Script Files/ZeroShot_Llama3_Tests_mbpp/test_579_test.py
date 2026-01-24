import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):

    def test_find_dissimilar(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (1, 2, 4)), ((3,), (4,)))
        self.assertEqual(find_dissimilar((1, 2, 3), (1, 2, 3)), ())
        self.assertEqual(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4)), ())
        self.assertEqual(find_dissimilar((1, 2, 3, 4), (1, 2, 3)), ((4,),))
        self.assertEqual(find_dissimilar((1, 2, 3, 4, 5), (1, 2, 3, 4, 5)), ())
        self.assertEqual(find_dissimilar((1, 2, 3, 4, 5), (1, 2, 3, 4),), ((5,),))
        self.assertEqual(find_dissimilar((1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6)), ())
        self.assertEqual(find_dissimilar((1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5),), ((6,),))

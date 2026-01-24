import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):

    def test_find_dissimilar(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (3, 4, 5)), ((1, 2), (4, 5)))
        self.assertEqual(find_dissimilar(('a', 'b', 'c'), ('c', 'd', 'e')), (('a', 'b'), ('d', 'e')))
        self.assertEqual(find_dissimilar((True, False), (False, True)), ((True,), (True,)))
        self.assertEqual(find_dissimilar((), (1, 2, 3)), ((1, 2, 3),))
        self.assertEqual(find_dissimilar((1, 2, 3), ()), ((1, 2, 3),))
        self.assertEqual(find_dissimilar((), ()), ((),))

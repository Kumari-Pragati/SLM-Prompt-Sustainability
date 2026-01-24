import unittest
from mbpp_579_code import Tuple

from 579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):

    def test_empty_tuples(self):
        self.assertListEqual(find_dissimilar((), ()), [])

    def test_single_element_tuples(self):
        self.assertListEqual(find_dissimilar((1,), (1,)), [])
        self.assertListEqual(find_dissimilar((1,), (2,)), [1, 2])

    def test_identical_tuples(self):
        self.assertListEqual(find_dissimilar((1, 2, 3), (1, 2, 3)), [])

    def test_dissimilar_tuples(self):
        self.assertListEqual(find_dissimilar((1, 2, 3), (4, 5, 6)), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(find_dissimilar((1, 2, 'a'), (1, 2, 'b')), ['a', 'b'])

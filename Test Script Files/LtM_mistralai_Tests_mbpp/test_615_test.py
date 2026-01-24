import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(average_tuple([(1, 2), (3, 4)]), [2.5, 3.5])
        self.assertListEqual(average_tuple([(5,), (6,), (7,)]), [5.0, 6.0, 7.0])

    def test_edge_cases(self):
        self.assertListEqual(average_tuple([]), [])
        self.assertListEqual(average_tuple([(1,), (2,)]), [1.5])
        self.assertListEqual(average_tuple([(1,), (2,), (3,), (4,), (5,)]), [2.4, 3.4, 4.4, 5.4])

    def test_complex_input(self):
        self.assertListEqual(average_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]), [3.4, 4.4, 5.4, 6.4, 7.4])
        self.assertListEqual(average_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)]), [4.2, 5.2, 6.2, 7.2, 8.2, 9.2])
        self.assertListEqual(average_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14)]), [4.6, 5.6, 6.6, 7.6, 8.6, 9.6, 10.6])

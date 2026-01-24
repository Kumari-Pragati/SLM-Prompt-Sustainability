import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):

    def test_positive_count(self):
        self.assertEqual(positive_count(array('i', [1, 2, 3, 4, 5])), 0.5)
        self.assertEqual(positive_count(array('i', [1, 2, 3, 4, 5, 6])), 0.6666666666666666)
        self.assertEqual(positive_count(array('i', [1, 2, 3])), 1.0)
        self.assertEqual(positive_count(array('i', [1])), 1.0)
        self.assertEqual(positive_count(array('i', [1, -1, 2, 3])), 0.5)
        self.assertEqual(positive_count(array('i', [-1, -2, -3])), 0.0)
        self.assertEqual(positive_count(array('i', [1, 2, 3, 4, 5, -1])), 0.5)
        self.assertEqual(positive_count(array('i', [1, 2, 3, 4, 5, 6, -1])), 0.5714285714285714)

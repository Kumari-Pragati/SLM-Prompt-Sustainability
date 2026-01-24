import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):
    def test_average_tuple(self):
        self.assertEqual(average_tuple([(1, 2, 3), (4, 5, 6)]), [2.5, 5.0])
        self.assertEqual(average_tuple([(1, 2), (3, 4)]), [1.5, 3.5])
        self.assertEqual(average_tuple([(1, 2, 3, 4), (5, 6, 7, 8)]), [2.5, 4.0, 5.5, 6.5])
        self.assertEqual(average_tuple([([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])), [5.0]])
        self.assertRaises(TypeError, average_tuple, [[1, 2, 3], 'a', [4, 5, 6]])

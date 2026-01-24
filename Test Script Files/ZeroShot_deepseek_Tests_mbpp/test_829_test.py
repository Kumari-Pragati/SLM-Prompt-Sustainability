import unittest
from mbpp_829_code import Counter
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):

    def test_second_frequent(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3, 3]), 2)
        self.assertEqual(second_frequent(['a', 'b', 'b', 'c', 'c', 'c']), 'b')
        self.assertEqual(second_frequent([1, 1, 2, 2, 3, 3]), 2)
        self.assertEqual(second_frequent(['a', 'a', 'b', 'b', 'c', 'c']), 'b')
        self.assertEqual(second_frequent([1]), None)
        self.assertEqual(second_frequent(['a']), None)
        self.assertEqual(second_frequent([]), None)
        self.assertEqual(second_frequent([1, 2, 2, 3, 3]), 2)
        self.assertEqual(second_frequent(['a', 'b', 'b', 'c', 'c']), 'b')

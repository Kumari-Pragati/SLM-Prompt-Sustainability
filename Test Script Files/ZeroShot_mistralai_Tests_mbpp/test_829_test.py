import unittest
from mbpp_829_code import Counter
from your_module import second_frequent

class TestSecondFrequent(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(second_frequent([]))

    def test_single_element(self):
        self.assertIsNone(second_frequent([1]))

    def test_two_elements(self):
        self.assertEqual(second_frequent([1, 1]), 1)
        self.assertEqual(second_frequent([2, 1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(second_frequent([1, 2, 1, 2, 3, 2]), 2)
        self.assertEqual(second_frequent([1, 2, 2, 3, 2]), 3)

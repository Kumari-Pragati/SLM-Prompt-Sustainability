import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):

    def test_max_of_nth(self):
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), 3)
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), 8)
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), 1)
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), 9)
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4), None)
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5), None)

    def test_max_of_nth_empty_list(self):
        self.assertEqual(max_of_nth([], 0), None)

    def test_max_of_nth_single_element(self):
        self.assertEqual(max_of_nth([[1, 2, 3]], 0), 1)
        self.assertEqual(max_of_nth([[1, 2, 3]], 1, 2), 3)

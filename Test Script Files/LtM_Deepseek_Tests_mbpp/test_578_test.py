import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 6, 9])

    def test_empty_lists(self):
        self.assertEqual(interleave_lists([], [], []), [])

    def test_one_empty_list(self):
        self.assertEqual(interleave_lists([1, 2, 3], [], [4, 5, 6]), [1, 4, 2, 5, 3, 6])

    def test_maximum_values(self):
        self.assertEqual(interleave_lists([100]*10, [200]*10, [300]*10), [100, 200, 300]*10)

    def test_minimum_values(self):
        self.assertEqual(interleave_lists([-100]*10, [-200]*10, [-300]*10), [-100, -200, -300]*10)

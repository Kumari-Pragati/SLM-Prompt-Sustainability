import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 5), 2)
        self.assertEqual(left_insertion([1, 3, 5, 7], 0), 0)
        self.assertEqual(left_insertion([1, 3, 5, 7], 10), 4)

    def test_edge_cases(self):
        self.assertEqual(left_insertion([], 5), 0)
        self.assertEqual(left_insertion([1, 3, 5, 7], 1), 0)
        self.assertEqual(left_insertion([1, 3, 5, 7], 7), 3)

    def test_explicitly_handled_error_cases(self):
        # Since bisect_left doesn't handle errors, we don't need to test for them
        pass

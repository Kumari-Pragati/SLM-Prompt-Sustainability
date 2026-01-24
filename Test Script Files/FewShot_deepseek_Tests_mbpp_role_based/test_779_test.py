import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [1, 2, 3]]
        expected_output = {(1, 2, 3): 2, (4, 5, 6): 1}
        self.assertEqual(unique_sublists(list1), expected_output)

    def test_empty_list(self):
        list1 = []
        expected_output = {}
        self.assertEqual(unique_sublists(list1), expected_output)

    def test_single_sublist(self):
        list1 = [[1, 2, 3]]
        expected_output = {(1, 2, 3): 1}
        self.assertEqual(unique_sublists(list1), expected_output)

    def test_duplicate_sublists(self):
        list1 = [[1, 2, 3], [1, 2, 3]]
        expected_output = {(1, 2, 3): 2}
        self.assertEqual(unique_sublists(list1), expected_output)

    def test_large_sublists(self):
        list1 = [[i for i in range(1, 1001)]] * 1000
        expected_output = {(i for i in range(1, 1001)): 1000}
        self.assertEqual(unique_sublists(list1), expected_output)

    def test_mixed_types(self):
        list1 = [['a', 1, True], ['a', 1, False], [1, 2, 3]]
        expected_output = {('a', 1, True): 1, (1, 2, 3): 1, ('a', 1, False): 1}
        self.assertEqual(unique_sublists(list1), expected_output)

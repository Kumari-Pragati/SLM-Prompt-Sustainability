import unittest
from mbpp_758_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):
    
    def test_typical_case(self):
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

    def test_sublists_with_duplicates(self):
        list1 = [[1, 2, 3], [3, 2, 1]]
        expected_output = {(1, 2, 3): 1, (3, 2, 1): 1}
        self.assertEqual(unique_sublists(list1), expected_output)

    def test_invalid_input(self):
        list1 = [1, 2, 3]
        with self.assertRaises(TypeError):
            unique_sublists(list1)

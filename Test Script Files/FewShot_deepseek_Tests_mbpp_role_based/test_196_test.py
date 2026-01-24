import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 2), (3, 4, 5), (6,), ()]
        K = 2
        expected_output = [(1, 2), (6,)]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_edge_condition(self):
        test_list = [(1, 2), (3, 4, 5), (6,), ()]
        K = 0
        expected_output = [(1, 2), (3, 4, 5), (6,), ()]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_boundary_condition(self):
        test_list = [(1, 2), (3, 4, 5), (6,), ()]
        K = 1
        expected_output = [(1, 2), (3, 4, 5), (6,), ()]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_invalid_input(self):
        test_list = [(1, 2), (3, 4, 5), (6,), ()]
        K = 'a'
        with self.assertRaises(TypeError):
            remove_tuples(test_list, K)

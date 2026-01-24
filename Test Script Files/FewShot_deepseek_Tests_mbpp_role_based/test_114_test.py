import unittest
from mbpp_114_code import assign_freq

class TestAssignFreq(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [1, 2, 2, 3, 3, 3]
        expected_output = "[(1, 1), (2, 2), (3, 3)]"
        self.assertEqual(assign_freq(test_list), expected_output)

    def test_edge_case(self):
        test_list = []
        expected_output = "[]"
        self.assertEqual(assign_freq(test_list), expected_output)

    def test_boundary_case(self):
        test_list = [1] * 10000
        expected_output = "[(1, 10000)]"
        self.assertEqual(assign_freq(test_list), expected_output)

    def test_invalid_input(self):
        test_list = '12345'
        with self.assertRaises(TypeError):
            assign_freq(test_list)

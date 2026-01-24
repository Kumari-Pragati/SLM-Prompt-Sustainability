import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):
    def test_typical_case(self):
        test_list = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c')]
        expected_output = {1: ['a'], 2: ['b'], 3: ['a'], 4: ['c']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case(self):
        test_list = [(1, 'a'), (1, 'b'), (2, 'c')]
        expected_output = {1: ['a', 'b'], 2: ['c']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case2(self):
        test_list = [(1, 'a'), (1, 'a'), (2, 'b')]
        expected_output = {1: ['a', 'a'], 2: ['b']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case3(self):
        test_list = [(1, 'a'), (2, 'b'), (3, 'c')]
        expected_output = {1: ['a'], 2: ['b'], 3: ['c']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case4(self):
        test_list = [(1, 'a'), (1, 'a'), (1, 'a')]
        expected_output = {1: ['a', 'a', 'a']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case5(self):
        test_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
        expected_output = {1: ['a'], 2: ['b'], 3: ['c'], 4: ['d']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case6(self):
        test_list = [(1, 'a'), (1, 'a'), (1, 'a'), (1, 'a')]
        expected_output = {1: ['a', 'a', 'a', 'a']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case7(self):
        test_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
        expected_output = {1: ['a'], 2: ['b'], 3: ['c'], 4: ['d'], 5: ['e']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case8(self):
        test_list = [(1, 'a'), (1, 'a'), (1, 'a'), (1, 'a'), (1, 'a')]
        expected_output = {1: ['a', 'a', 'a', 'a', 'a']}
        self.assertEqual(group_element(test_list), expected_output)

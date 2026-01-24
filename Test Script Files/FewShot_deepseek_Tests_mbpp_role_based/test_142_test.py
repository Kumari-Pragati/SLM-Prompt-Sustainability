import unittest
from mbpp_142_code import count_samepair

class TestCountSamePair(unittest.TestCase):
    def test_typical_case(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        list3 = [1, 2, 3, 4, 5]
        self.assertEqual(count_samepair(list1, list2, list3), 5)

    def test_edge_case(self):
        list1 = []
        list2 = []
        list3 = []
        self.assertEqual(count_samepair(list1, list2, list3), 0)

    def test_boundary_case(self):
        list1 = [1]
        list2 = [1]
        list3 = [2]
        self.assertEqual(count_samepair(list1, list2, list3), 0)

    def test_invalid_input(self):
        list1 = [1, 2, 3]
        list2 = [1, 2]
        list3 = [1, 2, 3]
        with self.assertRaises(ValueError):
            count_samepair(list1, list2, list3)

import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):

    def test_normal_input(self):
        self.assertDictEqual(check_occurences([[1, 2], [2, 1], [3, 4]]), {'(1, 2)': 2, ('3', '4'): 1})

    def test_edge_and_boundary_cases(self):
        self.assertDictEqual(check_occurences([[1, 1], [2, 2], [3, 3]]), {'(1, 1)': 1, ('2', '2'): 1, ('3', '3'): 1})
        self.assertDictEqual(check_occurences([[1, 2], [2, 1], [1, 2]]), {'(1, 2)': 2})
        self.assertDictEqual(check_occurences([[1], [2], [3]]), {('1',): 1, ('2',): 1, ('3',): 1})
        self.assertDictEqual(check_occurences([[1, 2, 3], [2, 1, 3], [1, 2, 3]]), {'(1, 2, 3)': 3})

    def test_special_cases(self):
        self.assertDictEqual(check_occurences([[1, 2], [2, 1], [2, 1]]), {'(1, 2)': 2, ('2', '1'): 2})
        self.assertDictEqual(check_occurences([[1, 2, 3], [3, 2, 1], [2, 3, 1]]), {'(1, 2, 3)': 1, ('3', '2', '1'): 1, ('2', '3', '1'): 1})

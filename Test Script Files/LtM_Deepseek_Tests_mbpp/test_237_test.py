import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(check_occurences([[1, 2, 3], [1, 2, 3], [4, 5, 6]]), {(1, 2, 3): 2, (4, 5, 6): 1})
        self.assertEqual(check_occurences([[1, 2, 2], [1, 2, 2], [1, 2, 3]]), {(1, 2, 2): 2, (1, 2, 3): 1})

    def test_edge_conditions(self):
        self.assertEqual(check_occurences([]), {})
        self.assertEqual(check_occurences([[]]), {((): 1)})

    def test_complex_cases(self):
        self.assertEqual(check_occurences([[1, 2, 3], [3, 2, 1], [1, 2, 3]]), {(1, 2, 3): 2, (3, 2, 1): 1})
        self.assertEqual(check_occurences([[1, 2, 2], [2, 1, 2], [1, 2, 3]]), {(1, 2, 2): 2, (2, 1, 2): 1, (1, 2, 3): 1})

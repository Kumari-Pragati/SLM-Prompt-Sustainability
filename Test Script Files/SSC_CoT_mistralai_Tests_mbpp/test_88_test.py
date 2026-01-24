import unittest
from mbpp_88_code import Counter
from 88_code import freq_count

class TestFreqCount(unittest.TestCase):

    def test_normal_input(self):
        self.assertCountEqual(freq_count([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})
        self.assertCountEqual(freq_count(['a', 'b', 'a', 'c', 'b', 'a']), {'a': 3, 'b': 2, 'c': 1})

    def test_edge_and_boundary_conditions(self):
        self.assertCountEqual(freq_count([]), {})
        self.assertCountEqual(freq_count([1]), {1: 1})
        self.assertCountEqual(freq_count([1, 1, 1, 1]), {1: 4})
        self.assertCountEqual(freq_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1})

    def test_special_cases(self):
        self.assertCountEqual(freq_count([0]), {})
        self.assertCountEqual(freq_count([float('nan')]), {float('nan'): 1})
        self.assertCountEqual(freq_count([True]), {True: 1})
        self.assertCountEqual(freq_count([None]), {None: 1})

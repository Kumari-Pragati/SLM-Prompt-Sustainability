import unittest
from mbpp_88_code import Counter
from 88_code import freq_count

class TestFreqCount(unittest.TestCase):

    def test_simple(self):
        self.assertDictEqual(freq_count([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})
        self.assertDictEqual(freq_count(['a', 'b', 'a', 'c', 'b', 'b']), {'a': 2, 'b': 3, 'c': 1})

    def test_edge_and_boundary(self):
        self.assertDictEqual(freq_count([]), {})
        self.assertDictEqual(freq_count([1]), {1: 1})
        self.assertDictEqual(freq_count([1, 1, 1]), {1: 3})
        self.assertDictEqual(freq_count([1, 2, 3, 4, 5]), {1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
        self.assertDictEqual(freq_count(['a', 'b', 'c', 'd', 'e']), {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})

    def test_complex(self):
        self.assertDictEqual(freq_count([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), {1: 1, 2: 2, 3: 3, 4: 3, 5: 3})
        self.assertDictEqual(freq_count(['a', 'b', 'a', 'c', 'b', 'b', 'd', 'e', 'd', 'e']), {'a': 2, 'b': 3, 'c': 1, 'd': 2, 'e': 2})

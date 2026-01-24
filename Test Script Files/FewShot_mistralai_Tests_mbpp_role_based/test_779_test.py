import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):
    def test_empty_list(self):
        self.assertDictEqual(unique_sublists([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(unique_sublists([1]), {(1,): 1})

    def test_simple_list(self):
        self.assertDictEqual(unique_sublists([1, 2, 3]), {(1, 2, 3): 1})

    def test_duplicate_sublists(self):
        self.assertDictEqual(unique_sublists([1, 2, 1, 3]), {(1, 2, 1): 2, (1, 3): 1})

    def test_mixed_sublists(self):
        self.assertDictEqual(unique_sublists([1, 2, 3, 4, 1, 2]), {(1, 2, 3): 1, (1, 2, 4): 1})

    def test_large_list(self):
        self.assertDictEqual(unique_sublists(list(range(10))), {tuple(sorted(sublist)) for sublist in itertools.combinations(list(range(10)), r=len(list(range(10))))})

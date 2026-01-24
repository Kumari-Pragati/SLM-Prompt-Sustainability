import unittest
from mbpp_778_code import islice, chain, repeat
from collections import deque

from778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 4]), [deque([1]), deque([2]), deque([3]), deque([4])])
        self.assertEqual(pack_consecutive_duplicates([1, 1, 1, 2, 2, 3, 3, 4, 4, 4]), [deque([1, 1, 1]), deque([2]), deque([3]), deque([4])])

    def test_edge_cases(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])
        self.assertEqual(pack_consecutive_duplicates([1]), [deque([1])])
        self.assertEqual(pack_consecutive_duplicates([1, 2]), [deque([1]), deque([2])])
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2]), [deque([1]), deque([1]), deque([2])])
        self.assertEqual(pack_consecutive_duplicates([1, 1, 1, 2]), [deque([1, 1, 1]), deque([2])])

    def test_boundary_cases(self):
        self.assertEqual(pack_consecutive_duplicates(list(repeat(1, 1000))), [deque(chain.from_iterable(islice(repeat([1], 1000, 100))))])
        self.assertEqual(pack_consecutive_duplicates(list(chain.from_iterable(repeat([1], 1000000, 100000)))), [deque(chain.from_iterable(islice(repeat([1], 1000000, 100000))))])

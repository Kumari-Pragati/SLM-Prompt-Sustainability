import unittest
from mbpp_39_code import Counter
import heapq

def rearange_string(S):
    ctr = Counter(S)
    heap = [(-value, key) for key, value in ctr.items()]
    heapq.heapify(heap)
    if (-heap[0][0]) * 2 > len(S) + 1:
        return ""
    ans = []
    while len(heap) >= 2:
        nct1, char1 = heapq.heappop(heap)
        nct2, char2 = heapq.heappop(heap)
        ans.extend([char1, char2])
        if nct1 + 1: heapq.heappush(heap, (nct1 + 1, char1))
        if nct2 + 1: heapq.heappush(heap, (nct2 + 1, char2))
    return "".join(ans) + (heap[0][1] if heap else "")

class TestRearrangeString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(rearange_string(""), "")

    def test_single_character(self):
        self.assertEqual(rearange_string("a"), "a")
        self.assertEqual(rearange_string("z"), "z")

    def test_two_characters(self):
        self.assertEqual(rearange_string("aa"), "aa")
        self.assertEqual(rearange_string("ab"), "ab")
        self.assertEqual(rearange_string("ba"), "ba")

    def test_multiple_characters(self):
        self.assertEqual(rearange_string("aaaabbccc"), "abccbaa")
        self.assertEqual(rearange_string("zzzzzyyyy"), "zyyyzzzz")
        self.assertEqual(rearange_string("AABBCCDD"), "CDDCCBBAA")

    def test_long_string(self):
        self.assertEqual(rearange_string("aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
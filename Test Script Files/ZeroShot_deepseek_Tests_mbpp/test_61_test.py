import unittest
from mbpp_61_code import defaultdict

def count_Substrings(s,n):
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count

class TestCountSubstrings(unittest.TestCase):
    def test_count_Substrings(self):
        self.assertEqual(count_Substrings('123', 3), 4)
        self.assertEqual(count_Substrings('111', 3), 6)
        self.assertEqual(count_Substrings('121', 3), 3)
        self.assertEqual(count_Substrings('12345', 5), 15)
        self.assertEqual(count_Substrings('11111', 5), 10)

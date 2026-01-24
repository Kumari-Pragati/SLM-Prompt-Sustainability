import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_replica(('a', 'b', 'a', 'c', 'b')), ('a', 'b', 'MSP', 'c', 'MSP'))

    def test_empty_tuple(self):
        self.assertEqual(remove_replica(()), ())

    def test_single_element(self):
        self.assertEqual(remove_replica(('a',)), ('a',))

    def test_all_duplicates(self):
        self.assertEqual(remove_replica(('a', 'a', 'a', 'a')), ('MSP', 'MSP', 'MSP', 'MSP'))

    def test_no_duplicates(self):
        self.assertEqual(remove_replica(('a', 'b', 'c')), ('a', 'b', 'c'))

    def test_large_tuple(self):
        test_tup = ('a',) * 10000 + ('a',)
        self.assertEqual(remove_replica(test_tup)[10000:], ('MSP',))

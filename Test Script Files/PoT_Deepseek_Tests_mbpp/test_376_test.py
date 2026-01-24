import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_replica(('a', 'b', 'a')), ('a', 'b', 'MSP'))

    def test_empty_tuple(self):
        self.assertEqual(remove_replica(()), ())

    def test_single_element(self):
        self.assertEqual(remove_replica(('a',)), ('a',))

    def test_all_duplicates(self):
        self.assertEqual(remove_replica(('a', 'a', 'a')), ('a', 'MSP', 'MSP'))

    def test_no_duplicates(self):
        self.assertEqual(remove_replica(('a', 'b', 'c')), ('a', 'b', 'c'))

    def test_large_tuple(self):
        self.assertEqual(remove_replica(('a',) * 1000 + ('a',)), ('a',) * 999 + ('MSP',))

    def test_mixed_types(self):
        self.assertEqual(remove_replica(('a', 1, 'a')), ('a', 1, 'MSP'))

    def test_complex_types(self):
        self.assertEqual(remove_replica((1, 'a', 1)), (1, 'a', 'MSP'))

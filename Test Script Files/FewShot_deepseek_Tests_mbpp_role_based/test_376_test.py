import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_replica(('a', 'b', 'a', 'c', 'b')), ('a', 'b', 'c', 'MSP', 'MSP'))

    def test_empty_tuple(self):
        self.assertEqual(remove_replica(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(remove_replica(('a',)), ('a',))

    def test_all_same_elements_tuple(self):
        self.assertEqual(remove_replica(('a', 'a', 'a')), ('a', 'MSP'))

    def test_all_different_elements_tuple(self):
        self.assertEqual(remove_replica(('a', 'b', 'c')), ('a', 'b', 'c'))

    def test_large_tuple(self):
        self.assertEqual(remove_replica(('a',) * 1000 + ('a',)), ('a',) * 999 + ('MSP',))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_replica(123)

import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):

    def test_simple_unique_input(self):
        self.assertEqual(remove_replica((1, 2, 3)), (1, 2, 3))

    def test_simple_duplicate_input(self):
        self.assertEqual(remove_replica((1, 1, 2, 3)), (1, 2, 3))

    def test_empty_input(self):
        self.assertEqual(remove_replica(()), ('MSP',))

    def test_single_input(self):
        self.assertEqual(remove_replica((1,)), (1,))

    def test_min_max_values(self):
        self.assertEqual(remove_replica((-32767, -1, 0, 1, 32767)), (-32767, -1, 0, 1, 32767))

    def test_large_input(self):
        large_input = tuple(range(-32767, 32768))
        self.assertEqual(remove_replica(large_input), large_input)

    def test_duplicate_at_beginning(self):
        self.assertEqual(remove_replica((2, 2, 3)), (3,))

    def test_duplicate_at_end(self):
        self.assertEqual(remove_replica((1, 2, 2)), (1, 2))

    def test_duplicate_in_middle(self):
        self.assertEqual(remove_replica((1, 2, 2, 3)), (1, 2, 3))

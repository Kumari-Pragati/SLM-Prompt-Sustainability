import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):
    def test_typical_input(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, sorted(subjectmarks, key=lambda x: x[1]))

    def test_empty_input(self):
        subjectmarks = []
        result = subject_marks(subjectmarks)
        self.assertEqual(result, [])

    def test_single_element_input(self):
        subjectmarks = [('English', 88)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, subjectmarks)

    def test_multiple_elements_input(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82), ('History', 85)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, sorted(subjectmarks, key=lambda x: x[1]))

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            subject_marks('Invalid input')

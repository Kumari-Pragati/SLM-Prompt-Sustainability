import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):

    def test_simple_input(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        expected_output = [('English', 88), ('Social sciences', 82), ('Science', 90), ('Maths', 97)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_empty_input(self):
        subjectmarks = []
        expected_output = []
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_single_subject(self):
        subjectmarks = [('Maths', 97)]
        expected_output = [('Maths', 97)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_duplicate_marks(self):
        subjectmarks = [('English', 88), ('Science', 88), ('Maths', 88), ('Social sciences', 88)]
        expected_output = [('Science', 88), ('Maths', 88), ('Social sciences', 88), ('English', 88)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_maximum_marks(self):
        subjectmarks = [('English', 100), ('Science', 100), ('Maths', 100), ('Social sciences', 100)]
        expected_output = [('Maths', 100), ('Science', 100), ('Social sciences', 100), ('English', 100)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_minimum_marks(self):
        subjectmarks = [('English', 0), ('Science', 0), ('Maths', 0), ('Social sciences', 0)]
        expected_output = [('Maths', 0), ('Science', 0), ('Social sciences', 0), ('English', 0)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

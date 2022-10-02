import unittest
from first_project import avg


class EasyTestCase(unittest.TestCase):

    def test_easy_input(self):
        self.assertEqual(avg(1, 2, 3), 2)


class MediumTestCase(unittest.TestCase):

    # use self.assertRaises
    def test_medium_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, "string", 5), 2)


class HardTestCase(unittest.TestCase):

    def test_hard_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(False, None, frozenset), 10)

if __name__ == "__main__":
    unittest.main()








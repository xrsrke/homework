import unittest
import main

# Hint: use .assertIsInstance to check if the object is of the expected type

class TestMain(unittest.TestCase):
    
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_2(self):
        test_param = 'string'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

unittest.main()

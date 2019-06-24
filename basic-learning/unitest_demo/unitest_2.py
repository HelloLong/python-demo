import unittest

def func():
    raise Exception('lets see if this works')

class ExampleTest(unittest.TestCase):
    def test_error(self):
        self.assertRaises(Exception, lambda:func())

if __name__=='__main__':
    unittest.main()
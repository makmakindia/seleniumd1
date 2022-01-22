import unittest
from demoexample import Examples


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(" setUpClass:This will runs once before every class ..... 1")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass:This will run after every class......2")
    def setUp(self):
        print(" This will run before every method ..... 1 ")
    def tearDown(self):
        print("This will run after every method......2")

    def test_add(self):

        self.assertEqual(Examples.add(self, 30, 20),50)
        self.assertEqual(Examples.add(self, -1, 1),0)
        self.assertEqual(Examples.add(self, 10, 20),30)

    def test_sub(self):
        self.assertEqual(Examples.subfun(self, 30, 20), 10)
        self.assertEqual(Examples.subfun(self, -1, 1), -2)
        self.assertEqual(Examples.subfun(self, 50, 1), 49)


if __name__ == '__main__':
    unittest.main()
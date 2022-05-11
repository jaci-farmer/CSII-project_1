import unittest
from gui import *

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = GUI(Tk, 'Jaci', 20, 'student')
        self.p2 = GUI(Tk, 'Livia', 50, 'staff')
        self.p3 = GUI(Tk, 'Bill', 60, 'both')
    def tearDown(self):
        del self.p1
        del self.p2
        del self.p3
    def test_init(self):
        self.assertEqual(self.p1.name(), 'Jaci')
        self.assertEqual(self.p1.age(), 20)
        self.assertEqual(self.p1.grade(), 'student')
        self.assertEqual(self.p2.name(), 'Livia')
        self.assertEqual(self.p2.age(), 50)
        self.assertEqual(self.p2.grade(), 'staff')
        self.assertEqual(self.p1.name(), 'Bill')
        self.assertEqual(self.p1.age(), 60)
        self.assertEqual(self.p1.grade(), 'both')

    def test_name(self):
        with self.assertRaises(TypeError):
            name(10)

    def test_age(self):
        with self.assertRaises(TypeError):
            age('5')
        with self.assertRaises(ValueError):
            age(-5)


if __name__ == '__main__':
    unittest.main()

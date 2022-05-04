import unittest
from gui import *


class MyTestCase(unittest.TestCase):
    def test_clicked(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

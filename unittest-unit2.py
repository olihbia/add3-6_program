import unittest

from pythonunit2 import sum

class Testing(unittest.TestCase):
    def test_(self):
        data = [3, 6]
        result = sum
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()

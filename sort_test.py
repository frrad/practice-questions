import sort
import unittest


class TestSort(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(sort.sort([]), [])

    def test_backwards(self):
        test_list = list(reversed(range(10)))
        output = sorted(test_list)

        self.assertEqual(sort.sort(test_list), output)

    def test_random(self):
        test_list = [1, 5, 6, 7, 8, 3, 20, -10, 1, 2345, 3, 14]
        output = sorted(test_list)

        self.assertEqual(sort.sort(test_list), output)


if __name__ == '__main__':
    unittest.main()

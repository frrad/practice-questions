import sort
import unittest

class TestSort(unittest.TestCase):
  def test_empty(self):
    self.assertEqual(sort.sort([]), [])

  def test_backwards(self):
    backwards = reversed(range(10))
    self.assertEqual(sort.sort(backwards),range(10))


if __name__ == '__main__':
  unittest.main()

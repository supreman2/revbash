import unittest
import main

class TestFindRoom(unittest.TestCase):

    def test_findroom(self):
        self.assertEqual(main.main(1), (1,1))
        self.assertEqual(main.main(4), (3, 1))
        self.assertEqual(main.main(10), (5, 2))
        self.assertEqual(main.main(25), (9, 3))

if __name__ == '__main__':
    unittest.main()
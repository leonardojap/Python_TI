import unittest

import app

class TestApp(unittest.TestCase):
    
    def test_less(self):
        capture = app.DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        self.assertEqual(stats.less(4), 2)
        self.assertEqual(stats.less(9), 4)
        self.assertEqual(stats.less(6), 3)
        with self.assertRaises(TypeError):
            stats.less('a') #do not accept strings
    
    def test_greater(self):
        capture = app.DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        self.assertEqual(stats.greater(4), 2)
        self.assertEqual(stats.greater(3), 3)
        self.assertEqual(stats.greater(6), 1)
        self.assertEqual(stats.greater(9), 0) # should be 0, because 9 is the highest value in the list
        #do not accept strings
        with self.assertRaises(TypeError):
            stats.greater('a')


    def test_between(self):
        capture = app.DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        self.assertEqual(stats.between(3, 6), 4)
        self.assertEqual(stats.between(6, 9), 2)
        self.assertEqual(stats.between(4, 6), 2)
        self.assertEqual(stats.between(11, 19), 0) # should be 0, because 11 and 19 are not present in the list
        self.assertEqual(stats.between(9, 3), 0) # should be 0, because 9 is upper than 3
        #do not accept strings
        with self.assertRaises(TypeError):
            stats.between(6, 'a')
        with self.assertRaises(TypeError):
            stats.between('a', 6)
        with self.assertRaises(TypeError):
            stats.between('a', 'b')
        
if __name__ == '__main__':
    unittest.main()

import unittest
from logic import *

class MyTestCase(unittest.TestCase):

    def test_circle(self):
        with self.assertRaises(ValueError):
            circle('s')
            circle('&')

        with self.assertRaises(TypeError):
            circle(-1)
            circle(0)

        self.assertAlmostEqual(circle(2), 12.5663, delta=0.001)
        self.assertAlmostEqual(circle(3.4), 36.3168, delta=0.001)

    def test_square(self):
        with self.assertRaises(ValueError):
            square('s')
            square('&')

        with self.assertRaises(TypeError):
            square(-1)
            square(0)

        self.assertAlmostEqual(square(2), 4.0, delta=0.001)
        self.assertAlmostEqual(square(3.4), 11.5599, delta=0.001)

    def test_rectangle(self):
        with self.assertRaises(ValueError):
            rectangle('s', 'y')
            rectangle('s', 5)
            rectangle(4, 'y')
            rectangle(4, '&')
            rectangle('s', '(')

        with self.assertRaises(TypeError):
            rectangle(-1, -2)
            rectangle(-1, 2)
            rectangle(1, -2)
            rectangle(0, 0)
            rectangle(0, 1)
            rectangle(3, 0)
            rectangle(0, -2)
            rectangle(-1, 0)

        self.assertAlmostEqual(rectangle(2, 3), 6.0, delta=0.001)
        self.assertAlmostEqual(rectangle(3.4, 2.1), 7.14, delta=0.001)
        self.assertAlmostEqual(rectangle(3.4, 2), 6.8, delta=0.001)
        self.assertAlmostEqual(rectangle(2, 3.4), 6.8, delta=0.001)

    def test_triangle(self):
        with self.assertRaises(ValueError):
            triangle('s', 'y')
            triangle('s', 5)
            triangle(4, 'y')
            triangle(4, '*')
            triangle('^', 's')

        with self.assertRaises(TypeError):
            triangle(-1, -2)
            triangle(-1, 2)
            triangle(1, -2)
            triangle(0, 0)
            triangle(0, 1)
            triangle(3, 0)
            triangle(0, -2)
            triangle(-1, 0)

        self.assertAlmostEqual(triangle(2, 3), 3.0, delta=0.001)
        self.assertAlmostEqual(triangle(3.4, 2.1), 3.57, delta=0.001)
        self.assertAlmostEqual(triangle(3.4, 2), 3.4, delta=0.001)
        self.assertAlmostEqual(triangle(2, 3.4), 3.4, delta=0.001)


if __name__ == '__main__':
    unittest.main()

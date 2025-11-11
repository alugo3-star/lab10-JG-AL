# https://github.com/alugo3-star/lab10-JG-AL.git
# Partner 1: Joseph Gedaly
# Partner 2: Andres Lugo


import unittest
from calculator import add, subtract, mul, div, logarithm, hypotenuse, square_root

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 4), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 3)
        self.assertEqual(subtract(-3, -1), -2)
        self.assertEqual(subtract(0, 5), -5)


    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5, 3), 15)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(5, 0), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 6), 2)
        self.assertEqual(div(-1, -3), 3)
        self.assertEqual(div(2, -6), -3)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(logarithm(3, 27), 3.0)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-6, 8), 10.0)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-4)

        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)

    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
# def swap(a,b):
#     a,b=b,a
#     return a, b

# print(swap(1,2))

import unittest

def swap(a, b):
    a, b = b, a
    return a, b

class TestSwapFunction(unittest.TestCase):
    def test_swap_positive_numbers(self):
        self.assertEqual(swap(1, 2), (2, 1))

    def test_swap_zero_and_positive(self):
        self.assertEqual(swap(0, 5), (5, 0))

    def test_swap_negative_numbers(self):
        self.assertEqual(swap(-1, -2), (-2, -1))

if __name__ == "__main__":
    unittest.main()
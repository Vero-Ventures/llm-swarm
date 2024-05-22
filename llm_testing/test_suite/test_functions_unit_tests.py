import unittest
from test_functions_docstrings import fibonacci, merge, gcd, max_subarray_sum, factorial, read_csv, execute_query, send_email, fetch_json, search_files

class TestFunctions(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)

    def test_merge(self):
        self.assertEqual(merge([], []), [])
        self.assertEqual(merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge([1, 3], [2, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge([1, 2, 3], []), [1, 2, 3])

    def test_gcd(self):
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(18, 0), 18)

    def test_max_subarray_sum(self):
        self.assertEqual(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_subarray_sum([1]), 1)
        self.assertEqual(max_subarray_sum([-1, -2, -3]), -1)
        self.assertEqual(max_subarray_sum([0, -1, 2, 3, -9, 2, 2]), 5)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    # Note: For functions like read_csv, execute_query, send_email, fetch_json, and search_files,
    # you will need to mock external dependencies or ensure the necessary environment (like files,
    # databases, and network responses) is set up for testing.

if __name__ == '__main__':
    unittest.main()

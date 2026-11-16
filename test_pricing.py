import unittest

from pricing import apply_discount, subtotal


class PricingTest(unittest.TestCase):
    def test_subtotal(self):
        self.assertEqual(subtotal([(10, 2), (5, 1)]), 25)

    def test_zero_quantity_rejected(self):
        with self.assertRaises(ValueError):
            subtotal([(10, 0)])

    def test_discount(self):
        self.assertEqual(apply_discount(100, 10), 90)


if __name__ == "__main__":
    unittest.main()

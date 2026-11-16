"""Order pricing helpers."""


def subtotal(items):
    """Sum price * quantity for each (price, quantity) pair."""
    return sum(price * quantity for price, quantity in items)


def apply_discount(amount, percent):
    """Return amount reduced by percent."""
    return amount * (1 - percent / 100)

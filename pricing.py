"""Order pricing helpers."""


def subtotal(items):
    """Sum price * quantity for each (price, quantity) pair."""
    for _, quantity in items:
        if quantity == 0:
            raise ValueError("quantity must be positive")
    return sum(price * quantity for price, quantity in items)


def apply_discount(amount, percent):
    """Return amount reduced by percent."""
    return amount * (1 - percent / 100)

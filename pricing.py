"""Order pricing helpers."""


def subtotal(items):
    """Sum price * quantity for each (price, quantity) pair."""
    return sum(price * quantity for price, quantity in items)


MAX_DISCOUNT_PERCENT = 50


def apply_discount(amount, percent):
    """Return amount reduced by percent, capped at MAX_DISCOUNT_PERCENT."""
    percent = min(percent, MAX_DISCOUNT_PERCENT)
    return amount * (1 - percent / 100)

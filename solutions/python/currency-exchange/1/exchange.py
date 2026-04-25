def exchange_money(budget, exchange_rate):
    """
    Converts USD to EUR using EUR per USD rate.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Returns remaining USD after exchanging part of the budget.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Returns total value of given number of bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    Returns how many whole bills fit into the amount.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """
    Returns leftover amount that cannot form a full bill.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Converts USD to EUR, applies spread (fee), and returns
    the maximum usable value in whole bills.
    """
    effective_rate = exchange_rate * (1 + spread / 100)
    foreign_money = budget / effective_rate
    number_of_bills = foreign_money // denomination
    return int(number_of_bills * denomination)

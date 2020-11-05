def final_deposit_amount(*interest, amount=1000):
    for rate in interest:
        amount = amount * (1 + rate / 100)
    return round(amount, 2)

"""
WAP that will take user input of cost price and selling
price and determines whether its a loss or a profit
"""
def profit_loss(cost_price, selling_price):
    if (selling_price-cost_price) > 0:
        return f"Profit: {selling_price-cost_price} Rs." 
    else:
        return f"Loss: {selling_price-cost_price} Rs."


print(profit_loss(10, 11))

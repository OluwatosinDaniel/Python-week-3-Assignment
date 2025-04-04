def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, it is applied; otherwise, the original price is returned.
    
    :param price: Original price of the item.
    :param discount_percent: Discount percentage to be applied.
    :return: Final price after applying the discount.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Given values
original_price = 100.0
discount_percentage = 25.0

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
print(f"Final price after discount: ${final_price:.2f}")

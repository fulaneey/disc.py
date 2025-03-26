def calculate_discount(price, discount_percent):
    """
    This function calculates the final price after applying a discount.
    If the discount is 20% or more, it applies the discount.
    Otherwise, it returns the original price.
    """
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price  # Calculate the discount amount
        final_price = price - discount_amount  # Subtract discount from original price
    else:
        final_price = price  # No discount applied
    
    return final_price

# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate and display final price
    final_price = calculate_discount(price, discount_percent)
    print(f"Final price after discount (if applied): {final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numerical values.")

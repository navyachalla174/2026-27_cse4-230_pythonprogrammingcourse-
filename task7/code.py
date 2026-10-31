
# Retail Billing with Multiple Discount Rules

products = []

subtotal = 0
total_tax = 0

print("===== RETAIL BILLING SYSTEM =====")

n = int(input("Enter number of products: "))

for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (Electronics/Clothing/Grocery): ").lower()

    price = float(input("Enter price per unit: "))
    quantity = int(input("Enter quantity: "))

    # Validate inputs
    if price < 0 or quantity <= 0:
        print("Invalid product details!")
        continue

    # Calculate product amount
    amount = price * quantity

    # Category-specific tax
    if category == "electronics":
        tax_rate = 18

    elif category == "clothing":
        tax_rate = 5

    elif category == "grocery":
        tax_rate = 0

    else:
        print("Invalid category!")
        continue

    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "amount": amount,
        "tax": tax
    })

# Calculate threshold discount
if subtotal >= 5000:
    discount = subtotal * 0.10

elif subtotal >= 2000:
    discount = subtotal * 0.05

else:
    discount = 0

# Maximum discount limit
discount = min(discount, 1000)

# Calculate final bill
final_bill = subtotal + total_tax - discount

# Display invoice
print("\n========== ITEMIZED INVOICE ==========")

for p in products:

    print("\nProduct:", p["name"])
    print("Category:", p["category"])
    print("Price:", p["price"])
    print("Quantity:", p["quantity"])
    print("Amount:", round(p["amount"], 2))
    print("Tax:", round(p["tax"], 2))

print("\n-------------------------------------")
print("Subtotal: Rs.", round(subtotal, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Discount: Rs.", round(discount, 2))
print("Maximum Discount: Rs. 1000")
print("-------------------------------------")

print("Final Bill: Rs.", round(final_bill, 2))

print("=====================================")
print("Thank you for shopping!")


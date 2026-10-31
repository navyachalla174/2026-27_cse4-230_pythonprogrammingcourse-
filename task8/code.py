
# Manufacturing Cost and Profitability Analysis

print("===== MANUFACTURING COST ANALYSIS =====")

# Product details
product = input("Enter product name: ")

quantity = int(input("Enter production quantity: "))

# Cost details
material = float(input("Enter material cost per unit: "))

labour = float(input("Enter labour charge per unit: "))

wastage = float(input("Enter wastage percentage: "))

machine = float(input("Enter machine cost per unit: "))

selling_price = float(input("Enter selling price per unit: "))

target = float(input("Enter required profit percentage: "))

# Validate inputs
if (quantity <= 0 or material < 0 or labour < 0
    or wastage < 0 or wastage > 100
    or machine < 0 or selling_price < 0 or target < 0):

    print("Invalid Input! Please enter valid values.")

else:

    # Calculate material cost
    material_cost = material * quantity

    # Calculate labour cost
    labour_cost = labour * quantity

    # Calculate wastage cost
    wastage_cost = material_cost * wastage / 100

    # Calculate machine cost
    machine_cost = machine * quantity

    # Total manufacturing cost
    total_cost = (
        material_cost +
        labour_cost +
        wastage_cost +
        machine_cost
    )

    # Calculate selling revenue
    revenue = selling_price * quantity

    # Calculate profit
    profit = revenue - total_cost

    # Calculate profit percentage
    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

    # Check profit target
    if profit_percentage >= target:
        status = "Profit Target Achieved"
    else:
        status = "Profit Target Not Achieved"

    # Display report
    print("\n===== MANUFACTURING REPORT =====")

    print("Product Name:", product)
    print("Production Quantity:", quantity)

    print("--------------------------------")

    print("Material Cost: Rs.", round(material_cost, 2))
    print("Labour Cost: Rs.", round(labour_cost, 2))
    print("Wastage Cost: Rs.", round(wastage_cost, 2))
    print("Machine Cost: Rs.", round(machine_cost, 2))

    print("--------------------------------")

    print("Total Manufacturing Cost: Rs.", round(total_cost, 2))
    print("Selling Revenue: Rs.", round(revenue, 2))
    print("Total Profit: Rs.", round(profit, 2))
    print("Profit Percentage:", round(profit_percentage, 2), "%")

    print("--------------------------------")

    print("Required Profit Target:", target, "%")
    print("Production Status:", status)

    print("================================")
    print("Analysis Completed!")

